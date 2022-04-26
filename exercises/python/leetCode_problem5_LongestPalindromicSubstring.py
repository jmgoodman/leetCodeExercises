class Solution:
    def longestPalindrome(self, s: str) -> str:
        hashmap = dict()
        res     = ""
        
        # dynamic programming: increment substring length
        # sublen = 1 and sublen = 2 cases are determined by definition, so let's go with that
        for i in range(len(s)):
            hashmap[(i,i)]   = True
            res              = s[i]
        
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                hashmap[(i,i+1)] = True
                res              = s[i:(i+2)]
            else:
                hashmap[(i,i+1)] = False
                
        
        sublen = 3
        while sublen <= len(s):
            lastidx = len(s) - sublen + 1
            
            for i in range(lastidx):
                left   = i
                leftp  = left + 1
                right  = i+sublen-1
                rightm = right-1
                
                if hashmap[(leftp,rightm)]:
                    if s[left] == s[right]:
                        hashmap[(left,right)] = True
                        res                   = s[left:(right+1)]
                    else:
                        hashmap[(left,right)] = False
                else:
                    hashmap[(left,right)] = False
            
            sublen += 1
            
        return res # still way too slow

# brute-force solution which is just as slow...
class SolutionBad:
    def longestPalindrome(self, s: str) -> str:
        hashmap = dict()
        res     = ""
        itercount = 0
        
        # brute force:
        for left in range(len(s)):
            for right in range(left,len(s)):
                itercount += 1
                substring = s[left:(right+1)]
                if substring == substring[::-1] and len(substring) > len(res): # is this string comparison implicitly a hash table lookup???
                    res = substring
        
        print(itercount)
        return res
                    