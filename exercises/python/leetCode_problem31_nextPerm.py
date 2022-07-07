class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # handle the len=1 case
        if len(nums) == 1:
            return
        
        left = len(nums)-1
        while nums[left] <= nums[left-1]:
            left-=1
            if left == 0:
                nums[:] = nums[::-1] # loop around
                return
            
        # find the first element that you can swap with the current (outer) left bound
        # i.e., the one that's juuuuust larger
        # (it MUST exist if you exited the loop above to this bit of code)
        right = len(nums)-1
        while nums[right] <= nums[left-1]:
            right -= 1
            
        # swap right and outerleft
        num_outerleft = nums[left-1]
        num_right     = nums[right]
        
        nums[left-1]  = num_right
        nums[right]   = num_outerleft
        
        # now flip order of the remaining dudes
        nums[left:]   = nums[:(left-1):-1]
        return
        
        
        