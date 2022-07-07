class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        
        while fast < len(nums):
            if nums[fast] > nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
            fast += 1
        
        return slow+1


class Solution_slow:
    def removeDuplicates(self, nums: List[int]) -> int:
        # hmmm why is this so slow
        idx  = 1
        prev = nums[0]
        
        k = len(nums)
        while idx < k:
            val = nums[idx]
            
            if val == prev:
                nums[:] = nums[:idx]+nums[(idx+1):] # ah. It probably has something to do with the fact that I'm re-assigning every value in nums here, huh? taking things from O(n) time to O(n**2) time for NO REASON
                k -= 1
            else:
                prev = nums[idx]
                idx += 1
        
        return k