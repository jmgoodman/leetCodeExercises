# keep track of state, i.e., if you come across a string you already processed, load its saved result instead of redundantly recomputing it (turns out, redundant recomputations are SUPER DUPER COMMON!!!)
class State:
    def __init__(self,text:str,pattern:str):
        self.mem = dict()
        self.text = text
        self.pattern = pattern
    def compare(self,i,j):
        # if breadcrumb marking it on/off the recursive path to a match decision is found, use that evaluation instead of computing it anew
        if (i,j) in self.mem:
            return self.mem[(i,j)]
        else:
            # a bona fide match iff the pattern is exhausted and so too is the text
            # if the pattern is exhausted but the text is not, it must be a nonmatch
            # if the text is exhausted but the pattern is not, WAIT: the pattern could have stars and therefore elements that can be ignored while still yielding a match!
            if j == len(self.pattern):
                return i == len(self.text) # this branch prevents infinite recursion
            else:
                # make sure there's more text left to evaluate
                # otherwise, evaluate to false
                if i < len(self.text):
                    doesFirstMatch = self.pattern[j] in {self.text[i],"."}
                else:
                    doesFirstMatch = False
                
                # now look ahead for a star and handle that
                if j+1 < len(self.pattern):
                    if self.pattern[j+1] == "*":
                        # recurrent evaluation: if a star, form two branches
                        # one branch: ignore this pattern (case where * = 0)
                        # another branch: remove a valid repeated character (case where * >= 1)
                        branch1 = self.compare(i,j+2) # ignore by skipping .* (2 chars) without incrementing the text position
                        if doesFirstMatch:
                            branch2 = self.compare(i+1,j) # move ahead in the text PROVIDED you have a valid match, but don't move the pattern since you're still evaluating for more repeats
                        else:
                            branch2 = False
                        
                        # if EITHER branch finds a match, we have a match, otherwise, we definitely don't
                        res = branch1 or branch2
                        # save to the table so if we revisit we don't have to evaluate again
                        self.mem[(i,j)] = res
                        return res
                    else:
                        pass
                else:
                    pass
                        
                # if there either is not or cannot be a star in the lookahead, then evaluate like a normal string
                # that is, increment both the text and pattern spot and start comparing there
                if doesFirstMatch:
                    res = self.compare(i+1,j+1)
                else:
                    res = False
                
                self.mem[(i,j)] = res
                return res
        

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S = State(s,p)
        return S.compare(0,0)