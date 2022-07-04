class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # hey so do I need to do anything special to constrain the output here?
        # uh, no, because in the end, the minimum divisor is gonna be 1 since we're constrained to ints
        # when we start gettin' floats, that's when we start sweating a little bit
        
        # step 0, handle the big edge cases
        if abs(divisor) > abs(dividend):
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == int(-2**31):
                return int(2**31-1)
            else:
                return -dividend
        
        # step 1, get the sign and value of each
        dend2 = bin(dividend)
        resultNegative = False
        
        if dividend < 0:
            resultNegative = not resultNegative
            num2 = dend2[3:]
        else:
            num2 = dend2[2:]
        
        sor2  = bin(divisor)
        if divisor < 0:
            resultNegative = not resultNegative
            denom2         = sor2[3:]
        else:
            denom2         = sor2[2:]
        
        resultValue = ""
        
        outerright = len(denom2)
        currentNum = int( num2[:outerright],2 )
        divval     = abs(divisor)
                
        while True:
            if currentNum >= divval:
                resultValue += "1"
                currentNum  -= divval
            else:
                resultValue += "0"
            if outerright < len(num2):
                currentNum <<= 1
                if num2[outerright]=="1":
                    currentNum += 1
            else:
                res = int(resultValue,2)
                if resultNegative:
                    res = -1 * res
                return res
            outerright += 1
            
            # hey guys you know what's a big ol pain in the butt? having to manually type out the dec expansion of 2**31 in my test cases. just sayin'... maybe fix whatever parsing is going on in the testcases console???
            
        
            
        
        
        
        
        