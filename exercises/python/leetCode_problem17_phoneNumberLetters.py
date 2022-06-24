class Solution:
    def __init__(self):
        self.digit2letterTable = {"0":[""],
                                 "1":[""],
                                 "2":["a","b","c"],
                                 "3":["d","e","f"],
                                 "4":["g","h","i"],
                                 "5":["j","k","l"],
                                 "6":["m","n","o"],
                                 "7":["p","q","r","s"],
                                 "8":["t","u","v"],
                                 "9":["w","x","y","z"]}
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        if len(digits) > 0:
            
            thisDigit, otherDigits = digits[0], digits[1:]
            theseLetters = self.digit2letterTable[thisDigit]
            
            deeperLevel  = self.letterCombinations(otherDigits)
            if len(deeperLevel) == 0:
                deeperLevel = [""]
            
            for char_ in theseLetters:
                temp = [char_+deepstring for deepstring in deeperLevel]
                res += temp
            
                
        return res