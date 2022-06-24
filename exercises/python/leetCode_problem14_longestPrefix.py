class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # this simple horizontal scanning solution seems just as good as anything else
        # they did call this easy...
        prefix = ''
        
        maxidx  = min( [len(str_) for str_ in strs] )
        nstrs   = len(strs)
        breakme = False
        
        for sidx in range(maxidx):
            chars = [str_[sidx] for str_ in strs]
            
            for cidx in range(nstrs-1):
                if chars[cidx] != chars[cidx+1]:
                    breakme = True
                    break
                else:
                    pass
            
            if breakme:
                break
            else:
                prefix += chars[0]
            
        return prefix