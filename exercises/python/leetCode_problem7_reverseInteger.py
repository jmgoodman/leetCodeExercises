class Solution:
    def reverse(self, x: int) -> int:
        xstr = str(abs(x))
        xrev = int(xstr[::-1])
        
        thresh = 1<<31
        if x < 0:
            if xrev > thresh:
                xrev = 0
            else:
                xrev *= -1
        else:
            if xrev >= thresh:
                xrev = 0
            else:
                pass
        
        return xrev