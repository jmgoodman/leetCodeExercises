class Solution:
    def __init__(self):
        self.opensBuffer = ''
        self.pairsDict   = {'(':')','[':']','{':'}'} # the open brackets are the keys, which is very convenient
    def isValid(self, s: str) -> bool:
        for char_ in s:
            if char_ in self.pairsDict:
                self.opensBuffer = char_ + self.opensBuffer
            else:
                if len(self.opensBuffer) == 0:
                    return False
                else:
                    currentOpen,self.opensBuffer = self.opensBuffer[0],self.opensBuffer[1:]
                    properCloseBracket = self.pairsDict[currentOpen]
                    if properCloseBracket != char_:
                        return False
                    else:
                        pass
        
        # make sure there aren't any hanging open brackets
        if len(self.opensBuffer) == 0:
            return True
        else:
            return False