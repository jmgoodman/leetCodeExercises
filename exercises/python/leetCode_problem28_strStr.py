class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # handle the needle = empty case
        if len(needle)==0:
            return 0
                
        haystackpointer = 0
        
        # make it inclusive so that you don't just skip the last character when len(needle)==1, or so you don't just skip everything entirely when len(needle)==len(haystack)
        # also do it this way instead of your previous way so you only gotta run it all len(haystack) - len(needle) + 1 times
        # let's say H:= len(haystack) and N:= len(needle)
        while haystackpointer <= ( len(haystack) - len(needle) ):
            if haystack[ haystackpointer:(haystackpointer+len(needle)) ] == needle: # len(needle)
                return haystackpointer
            
            haystackpointer += 1
            
        return -1
    
        # in the end, this runs in O(HN) time
        # kinda
        # provided H >> N
        # which is probably a safe assumption for the most intensive use cases
        # and indeed, if this assumption is violated, then we start to get things running in mere O(N) or even O(1) time
        # but we might consider these to be "edge cases"
        # so provided H >> N
        # then O(HN) is both our worst-case and our average-case estimate
        # is there perhaps a better way? a way to get this to run in mere O(H) time, for instance?
        # instantiate a hash table, do some dynamic programming, that sort of thing?