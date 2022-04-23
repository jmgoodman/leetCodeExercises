class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # just trust that 2 directions gets you the optimum
        chars = dict() # hashmap, no?
        
        left  = 0
        right = 0
        
        res   = 0
        
        # zero in on the bounds of the longest substring
        while right < len(s):
            thisLetter = s[right]
            
            if thisLetter in chars:
                left = max(left, chars[thisLetter]+1) # set the left bound to a new one if the existing running string fails the substring criterion AND the left bound isn't already past that point
                
            res = max(res, right-left+1) # maintain a longest value, even if you shift the window away from the true longest substring, its length will be maintained via the recursive max
            
            chars[thisLetter] = right # rightmost index where this character lives
            right            += 1     # march the rightward bound ever further (could be a for loop) (the idea with this algorithm is that you march right and keep track of an adaptive leftmost index and the longest difference between left & right that you record across loops)
        
        return res