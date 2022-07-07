class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # this feels like a 2-pointer method
        # there are two classes of invalid paren string
        # one where a close-paren arrives which wasn't preceded by an open-paren
        # and one where an open paren never gets terminated
        # the former is very easy to check for
        # the latter is more difficult unless we have a pointer working in reverse operating on an inverse rule
        
        leftparens  = 0
        rightparens = 0
        maxlen      = 0
        
        for paren in s:
            if paren == '(':
                leftparens+=1
            elif paren == ')':
                rightparens+=1
            
            if rightparens == leftparens:
                maxlen = max(maxlen,2*rightparens)
            elif rightparens > leftparens:
                rightparens = 0
                leftparens  = 0 # reset upon discovery of an unmatched right paren
                
        # consider this case:
        # ()((())
        # if we JUST work from the left, we only get len = 2
        # we need to work from the right to immediately detect unpaired left parens, too!
        # just like I identified up top!
        leftparens  = 0
        rightparens = 0
        for paren in s[::-1]:
            if paren == '(':
                leftparens+=1
            elif paren == ')':
                rightparens+=1
            
            if leftparens == rightparens:
                maxlen = max(maxlen,2*rightparens)
            elif leftparens > rightparens:
                rightparens = 0
                leftparens  = 0 # reset upon discovery of an unmatched right paren
        
        return maxlen
                
        
        