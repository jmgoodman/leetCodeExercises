class Solution:
    def __init__(self):
        # hard-code the cases of subtraction like a fucking animal
        self.romanValues    = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        self.romanNumerals  = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
    def intToRoman(self, num: int) -> str:
        idx  = 0
        val  = self.romanValues[idx]
        romanNumeral = ''
        while num > 0:
            if num < val:
                idx += 1
                val = self.romanValues[idx]
                continue
            num -= val
            romanNumeral += self.romanNumerals[idx]
            
        return romanNumeral