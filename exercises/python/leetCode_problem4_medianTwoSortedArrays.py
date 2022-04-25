class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # trick question, divide-and-conquer does NOT work here...
        
        # do in-place stuff to save on memory assignment overhead, that seems to be how the top solutions manage it
        for num in nums2:
            nums1.append(num)
        
        nums1.sort()
        k = len(nums1)
        
        if k==0:
            return None
        
        if k%2:
            return nums1[k//2]
        else:
            return ( nums1[k//2-1]+nums1[k//2] )/2

# actually, there IS a divide-and-conquer solution. It looks like this and doesn't actually save time given the leetCode problem's constraints. You'd need arrays of size, like, a billion to really see savings
class Solution_divandconq:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # here, we handle annoying edge cases
        # godddd why can't discrete math just hold everywhere?
        if len(nums1)==0 and len(nums2)==0:
            return None
        elif len(nums1)==0:
            return self.getMedian(nums2)
        elif len(nums2)==0:
            return self.getMedian(nums1)
        elif len(nums1)==1 and len(nums2)==1:
            return (nums1[0]+nums2[0])/2
        elif len(nums1)==1:
            if len(nums2) % 2: # if odd:
                idx  = len(nums2) // 2
                temp = sorted( nums2[(idx-1):(idx+2)]+[nums1[0]] )
                return self.getMedian(temp)
            else:
                idx  = len(nums2) // 2
                temp = sorted( nums2[(idx-1):(idx+1)]+[nums1[0]] )
                return self.getMedian(temp)
        elif len(nums2)==1:
            if len(nums1) % 2: # if odd:
                idx  = len(nums1) // 2
                temp = sorted( nums1[(idx-1):(idx+2)]+[nums2[0]] )
                return self.getMedian(temp)
            else:
                idx  = len(nums1) // 2
                temp = sorted( nums1[(idx-1):(idx+1)]+[nums2[0]] )
                return self.getMedian(temp)
        elif len(nums1)==2 and len(nums2)==2:
            temp = sorted(nums1+nums2)
            return self.getMedian(temp)
        elif len(nums1)==2:
            if len(nums2) % 2: # if odd:
                idx  = len(nums2)//2
                temp = sorted( nums2[(idx-1):(idx+2)]+[nums1[0],nums1[1]] )
                return self.getMedian(temp)
            else:
                idx = len(nums2)//2
                temp = sorted( nums2[(idx-2):(idx+2)]+[nums1[0],nums1[1]] )
                return self.getMedian(temp)
        elif len(nums2)==2:
            if len(nums1) % 2: # if odd:
                idx  = len(nums1)//2
                temp = sorted( nums1[(idx-1):(idx+2)]+[nums2[0],nums2[1]] )
                return self.getMedian(temp)
            else:
                idx = len(nums1)//2
                temp = sorted( nums1[(idx-2):(idx+2)]+[nums2[0],nums2[1]] )
                return self.getMedian(temp) 
        else:
            pass
            
        # here, compute medians and shave arrays recursively
        med1 = self.getMedian(nums1)
        med2 = self.getMedian(nums2)
        
        m = (len(nums1)-1)//2 # always preserve the median SET
        n = (len(nums2)-1)//2
        
        # not only should you preserve parity, you should keep slices symmetric
        # otherwise you shift the median window
        k = min(m,n)
                
        if med1 == med2:
            return med1
        elif med1 < med2:
            bigLeft  = nums2[:(-k)]
            lilRight = nums1[k:]
        else:
            bigLeft  = nums1[:(-k)]
            lilRight = nums2[k:]
        
        return self.findMedianSortedArrays(bigLeft,lilRight)
        
                    
    def getMedian(self,nums:List[int]) -> float:
        n = len(nums)
        if n == 0:
            return None
        
        if n % 2:
            idx = n//2
            val = nums[idx]
        else:
            idx = [n//2-1,n//2]
            val = (nums[idx[0]] + nums[idx[1]])/2
        
        return val