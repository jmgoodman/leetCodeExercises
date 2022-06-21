class slowSolution:
    def maxArea(self, height: List[int]) -> int:
        leftHeight = 0
        area       = 0
        listLen    = len(height)
        print(listLen)
        for (idx0,val0) in enumerate(height):
            if val0 <= leftHeight:
                continue
            else:
                pass
            
            subList = height[(idx0+1):]
            rightHeight = 0
            for (idx1,val1) in enumerate(subList[::-1]):
                boxht = min(val0,val1)
                if boxht <= rightHeight:
                    continue
                else:
                    pass
                
                boxwid = (listLen)-idx1-idx0-1    
                
                tempArea = boxwid*boxht
                
                if tempArea > area:
                    area   = tempArea
                    leftHeight  = val0
                    rightHeight = boxht
                else:
                    pass
                
                # print( (idx0,val0), (idx1,val1), tempArea )
                # you're too slow!
                
        return area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left  = 0
        right = len(height) - 1
        maxarea = 0
        
        while left < right:
            wid  = right - left
            lht  = height[left]
            rht  = height[right]
            ht   = min(lht,rht)
            area = wid*ht
            
            maxarea = max(area,maxarea)
            
            # take the smaller edge and shift it. logic being: this is what limits the area of the basin, so moving the other edge can only hurt
            # when equal, it doesn't really matter which you shift, it'll be worse, so just pick one & get it over with
            # in other words, we've found a framework where greed is good!
            # (this "pincer" maneuver is quite common! how quickly you forget from your other problems...)
            if lht <= rht: 
                left += 1
            else:
                right -= 1
                
        return maxarea