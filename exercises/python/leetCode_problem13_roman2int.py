class Solution:
    def __init__(self):
        self.map = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    def romanToInt(self, s: str) -> int:
        buffer = inf
        equivalent_int = 0
        for rchar in s:
            rval = self.map[rchar]
            equivalent_int += rval
            
            # subtraction logic
            if rval > buffer:
                equivalent_int -= 2*buffer
            
            buffer = rval
            
        return equivalent_int