class SolutionDynamicProgramming:
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

# brute-force solution which is just as slow (as opposed to an order of magnitude slower??? what is going ON???)...
class SolutionBruteForce:
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
                    
# see, y'all TELL me to do dynamic programming... but in the end I probably need to use the special O(n) algo that y'all tell me I do NOT need to know, no?

class SolutionRadiate:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        # radiate-from-center
        currentLength    = 1
        currentSubstring = s[0]
        
        # iterate thru odds
        for center in range(1,(len(s)-1)):
            # seed with new central substring
            newLength = currentLength + 2
            winglen   = newLength // 2
            left      = center-winglen
            right     = center+1+winglen
            
            if right > len(s):
                break
            
            substring = s[ left:right ]
            
            if substring == substring[::-1]:
                currentLength   += 2
                currentSubstring = substring
            else:
                continue
            
            # radiate
            left  -= 1
            right += 1
            while left >= 0 and right <= len(s):
                if s[left] == s[right-1]:
                    currentLength += 2
                    substring        = s[left]+substring+s[right-1]
                    currentSubstring = substring
                    left  -= 1
                    right += 1
                else:
                    break
                    
        # iterate thru evens
        currentLength -= 1
        newLength      = currentLength + 2
        winglen        = newLength // 2
        print(s,(winglen-1),(len(s)-winglen))
        for leftcenter in range( (winglen-1),(len(s)-winglen) ):
            newLength = currentLength + 2
            winglen   = newLength // 2
            left      = (leftcenter+1) - winglen
            right     = (leftcenter+1) + winglen
            
            if right > len(s):
                break
            
            substring = s[ left:right ]
            
            if substring == substring[::-1]:
                currentLength += 2
                currentSubstring = substring
            else:
                continue
            
            # radiate
            left  -= 1
            right += 1
            
            while left >= 0 and right <= len(s):
                if s[left] == s[right-1]:
                    currentLength   += 2
                    substring        = s[left]+substring+s[right-1]
                    currentSubstring = substring 
                    left  -= 1
                    right += 1
                else:
                    break
                    
        return currentSubstring

# okay but why did my dynamic programming solution fail so hard?
# I have to assume it has to do with hash table collisions...
