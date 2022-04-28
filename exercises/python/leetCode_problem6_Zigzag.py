class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1: # edge case
            return s
        
        rowInd   = 0
        rowsList = ["" for _ in range(numRows)]
        
        for char_ in s:
            rowsList[rowInd] += char_
            
            if rowInd == (numRows-1):
                diagMode = True # no need to init diagmode before the loop
            elif rowInd == 0:
                diagMode = False
                
            if diagMode:
                rowInd -= 1
            else:
                rowInd += 1

        newStr = "".join(rowsList) # faster than for -> +=, it seems (for older pythons anyway, the idea is += actually creates new instances in memory)
            
        return newStr