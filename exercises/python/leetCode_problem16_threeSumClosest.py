class Solution_tooslow:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort 
        nums.sort()
        print(nums)
        numslen = len(nums)
        closestsum = None
        sumdist    = inf # essential debugging step, since relying on 'None' and 'not' catches cases where delta = 0, i.e., the target
        
        # maintain a hashmap that stores values of index pairs
        pairsums = dict()
        
        # # and another hashmap that flips keys and values (only really valuable if you are looking to terminate in the special case where threesum=target, or abs(thressum-target)<some small #)
        # # however, in the worst case, this would just be extra steps
        # # this might yet improve average-case performance though
        # sumpairs = dict()
        
        for (idx,num) in enumerate(nums):
            if idx > numslen-3 or sumdist == 0:
                break
                
            unslice = nums[(idx+1):]
            subtarget = target - num
            
            left  = 0
            right = len(unslice)-1
            
            while left < right:
                absleft  = left+idx+1
                absright = right+idx+1
                if (absleft,absright) in pairsums:
                    pairsum = pairsums[(absleft,absright)] # saves an addition operation
                else:
                    lnum = unslice[left]
                    rnum = unslice[right]

                    pairsum = lnum+rnum
                    pairsums[(absleft,absright)] = pairsum
                
                subdist = pairsum - subtarget
                absdist = abs(subdist)
                
                if absdist < sumdist:
                    closestsum = pairsum+num
                    sumdist    = absdist
                else:
                    pass
                
                # if subdist says you smaller, move your left bound in
                # otherwise, move your right bound in
                # if it's zero, well, you just kinda solved the problem then, huh?
                if subdist < 0:
                    left += 1
                elif subdist > 0:
                    right -= 1
                elif subdist == 0:
                    break
            
        return closestsum


class Solution_stillquiteslowsomehow:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort 
        nums.sort()
        numslen = len(nums)
        closestSum = None
        bestDelta  = inf
        
        for idx in range(numslen-2):
            left  = idx+1
            right = numslen-1
            subTarget = target - nums[idx] # shaves an addition per while loop iteration (assumes most iterations will not be optimal triplets)
            
            while left < right:
                subSum    = nums[left] + nums[right]
                if subSum == subTarget:
                    return target
                
                currentDelta = abs(subSum - subTarget)
                if currentDelta < bestDelta:
                    closestSum = subSum + nums[idx]
                    bestDelta  = currentDelta
                else:
                    pass
                
                if subSum < subTarget:
                    left+=1
                else:
                    right-=1
                    
        return closestSum


# it seems from discussion threads that Java solutions are also suffering.
# there seems to be a problem with Leetcode...
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort 
        nums.sort()
        numslen = len(nums)
        closestSum = None
        bestDelta  = inf # float("inf")
                
        for idx in range(numslen-2):
            left  = idx+1
            right = numslen-1
            
            # compute a subTarget to shave an addition operation off most iterations
            subTarget = target - nums[idx]
            
            while left < right:
                subSum    = nums[left] + nums[right]
                
                currentDelta = abs(subSum - subTarget)
                if currentDelta < bestDelta:
                    closestSum = subSum + nums[idx]
                    bestDelta  = currentDelta
                    
                    # put this within the bestDelta check to avoid running it each and every time
                    if subSum == subTarget:
                        return target
                else:
                    pass
                
                if subSum < subTarget:
                    left+=1
                else:
                    right-=1
                    
        return closestSum