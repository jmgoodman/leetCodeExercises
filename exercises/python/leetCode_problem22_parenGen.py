class Solution:
    def __init__(self):
        self.stringsList = []
    def recursiveParenTreeCrawl(self,currentString:str = '',nOpenRemain:int = 0,nClosedRemain:int = 0) -> None:
        # if we've used all the parens available to us, spit out the result
        if nOpenRemain == 0 and nClosedRemain == 0:
            self.stringsList.append(currentString)
        else:
            pass
        
        # if we still have open parens to use, add another sucker in there
        if nOpenRemain > 0:
            newString = currentString+'('
            newRemain = nOpenRemain - 1
            self.recursiveParenTreeCrawl(newString,newRemain,nClosedRemain)
        else:
            pass
        
        # if we have any open parens that have yet to be closed, put a closing paren in there
        if nClosedRemain > nOpenRemain:
            newString = currentString+')'
            newClosed = nClosedRemain - 1
            self.recursiveParenTreeCrawl(newString,nOpenRemain,newClosed)
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.recursiveParenTreeCrawl('',n,n)
        return self.stringsList