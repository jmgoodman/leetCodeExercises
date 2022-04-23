# make the implicit explicit (except don't, it significantly adds to your runtime)
# from typing import Type, TypeVar

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a preliminary sort makes uniqueness easier to fulfill
        # sure, it adds logn to the computation time, ONCE
        # but otherwise, needing to test all permutations of triplets for uniqueness likely creates a bigger burden: 
        # increasing the slope will always outpace adding a logarithmic term in the long run
        #
        # okay
        # I have SUPREMELY screwed the pooch in terms of optimality
        # I think I have the general idea: piggyback off the twoSum case and just iterate using that optimal solution
        # there might be a recursive trick that I'm not seeing though...
        nums.sort(reverse=True)
        
        outmap = dict()
        while len(nums) > 2:
            thisTarget  = nums.pop() # we sort in reverse order to avoid weird memory shuffling issues with pop once we start iterating
            tupleList   = self.twoSum( nums, -thisTarget )
            for tuple_ in tupleList:
                checkTuple = (thisTarget,)+tuple_
                if checkTuple in outmap:
                    pass # outmap[checkTuple] += 1
                else:
                    outmap[checkTuple] = 1
        
        outList = [list(key_) for key_ in outmap.keys()]
            
        return outList
    
    def twoSum(self, nums: List[int], target: int) -> List[Tuple[int]]:
        hashmap = dict()
        outmap  = dict()
                
        for idx,val in enumerate(nums):
            complement = target - val
            if complement in hashmap:
                if (complement,val) in outmap:
                    pass # outmap[(val,complement)] += 1
                else:
                    outmap[(val,complement)] = 1
            else:
                pass
            
            if val in hashmap:
                pass # hashmap[val] += 1
            else:
                hashmap[val] = 1
                
        return outmap.keys()

## Alternatively, a set of better solutions (study them!) (it seems an element of divide-and-conquer is present s.t. the search for triples runs in O(nlogn) rather than O(n2) time)
class Solution_192:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0    
            counter[i] += 1

        nums = sorted(counter)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        output = []
        # find answer with no duplicates within combo
        for i in range(len(nums)-1):
            # search range
            twoSum = -nums[i]
            min_half, max_half = twoSum - nums[-1], twoSum / 2
            l = bisect_left(nums, min_half, i + 1)
            r = bisect_left(nums, max_half, l)
            
            for j in nums[l:r]:
                if twoSum - j in counter:
                    output.append([nums[i], j, twoSum - j])

        # find ans with duplicates within combo
        for k in counter:
            if counter[k] > 1:
                if k == 0 and counter[k] >= 3:
                    output.append([0, 0, 0])
                elif k != 0 and -2 * k in counter:
                    output.append([k, k, -2 * k])
        return output

class Solution_308:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num==0:
                if counter[num] > 2:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] > 1 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. not any of the three numbers are the same
            if num < 0:
                opposite = -num
                left = bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret

class Solution_652:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted = nums.copy()
        sorted.sort()
        solution = []
        for i, num in enumerate(sorted):
            if i == 0 or num != sorted[i - 1]:
                twoSum(sorted, i, solution)
        return solution
        # print(sorted)
        
def twoSum(nums: List[int], i: int, results: List[List[int]]) -> List[int]:
    leftPtr = i + 1
    rightPtr = len(nums) - 1
    target = 0 - nums[i]
    while leftPtr < rightPtr:
        res = nums[leftPtr] + nums[rightPtr]
        if res < target:
            leftPtr += 1
        elif res == target:
            results.append([nums[leftPtr], nums[rightPtr], nums[i]])
            prev = nums[leftPtr]
            while nums[leftPtr] == prev and leftPtr < rightPtr:
                leftPtr += 1
        else:
            rightPtr -= 1
    return [-1, -1]

class Solution_641:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res

class MySolution_905:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True) # probably be nice to make a copy to abstract that step away from developers, but not in this context where we wanna go fast and nothing else
        prevNum = None
        tripleList = []
        while len(nums) > 2:
            thisTarget  = nums.pop()
            if thisTarget > 0:
                break
            elif prevNum == thisTarget:
                continue
            else:
                prevNum = thisTarget
            
            tripleList += self.twoSum( nums, thisTarget )
            
        return tripleList
    
    def twoSum(self, nums: List[int], target: int) -> List[Tuple[int]]:
        # assumes pre-sorted list
        # spit out a triple where the first element is the target and the other 2 sum to its 0-complement
        # here we DEFINITELY make a copy
        numsCopy   = nums.copy()
        prevNum    = None
        hashmap    = dict()
        triple     = list()
        
        # we skip dupes so handle them (ughhhh there HAS to be a better way)
        dupeIncluded = False
        while len(numsCopy) > 0:
            thisReference = numsCopy.pop()
            if prevNum == thisReference:
                if not dupeIncluded:
                    if prevNum + thisReference == -target:
                        triple.append([target,complement,thisReference])
                        dupeIncluded = True
                    else:
                        pass
                else:
                    pass
                continue
            else:
                prevNum  = thisReference
            complement = -target-thisReference
            if complement in hashmap:
                triple.append([target,complement,thisReference])
            else:
                hashmap[thisReference] = 1 # janky way to do this, *sets* are implemented as hash tables and a much better choice for this!
                
        return triple