class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pairsmap = dict()
        res      = list()
        nlen     = len(nums)
        
        # this should run in roughly O(n**2) time
        # well okay apparently it's supposed to be O(n**3)
        # indeed, I abstracted away an awful lot of per-iteration sorting and uniqueness-checking in my initial estimate
        # but if I pre-sorted, this could still very much be achievable in O(n**2) time, no?
        
        # first, populate the pairsmap
        for idx0 in range(nlen-1):
            
            for idx1 in range(idx0+1,nlen):
                
                thisSum = nums[idx0] + nums[idx1]
                
                if thisSum not in pairsmap:
                    pairsmap[thisSum] = [[idx0,idx1]]
                    
                else:
                    pairsmap[thisSum] += [[idx0,idx1]]
        
        # now, go through and find all the quadruplets (probably a faster way to do this, likely by taking all combinations of keys that sum up to the target and working from there)
        testedtuples = set()
        for idx0 in range(nlen-1):
            for idx1 in range(idx0+1,nlen):
                # skip if (idx0,idx1) produces a tuple that's identical to what's been tested before
                tested = tuple( sorted([nums[idx0],nums[idx1]]) )
                
                if tested in testedtuples:
                    pass
                else:
                    testedtuples.add(tested)
                    
                    # and then run the rest
                    newTarget = target - nums[idx0] - nums[idx1]
                    if newTarget in pairsmap:
                        # eliminate the pairs which are redundant
                        keepPairs         = [pair for pair in pairsmap[newTarget] if pair[0]>idx1]

                        # candidates may include quadruplets where not all 4 are unique indices
                        newQuadInds       = [[idx0,idx1]+pair for pair in keepPairs]

                        # get the numeric values (and sort them... each quadruplet is only 4 elements, so each sort should not take too long, but still...)
                        newQuads          = [sorted([nums[idx] for idx in quad]) for quad in newQuadInds] # use sorted, not sort (in-place)

                        # take only the unique quads
                        uniqueQuads       = [tuple(quad) for quad in newQuads]
                        uniqueQuads       = list(set(uniqueQuads))
                        uniqueQuads       = [list(quad) for quad in uniqueQuads]
                        uniqueQuads       = [quad for quad in uniqueQuads if quad not in res]

                        # append to result
                        res              += uniqueQuads
                    
        # reduce res to the unique quads
        return res