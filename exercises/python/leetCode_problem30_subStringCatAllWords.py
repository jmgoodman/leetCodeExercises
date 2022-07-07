class Solution_slow:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # step 0: convert the words list into a dict
        wordsDict = dict()
        for word in words:
            if word in wordsDict:
                wordsDict[word] += 1 # handles cases where some entries ain't unique
            else:
                wordsDict[word] = 1
                
        
            
        # step 1: get len of the words (bounded from below by 1, inclusive, so we don't have to handle the empty-word edge case...)
        # also get the number of words needed in your string (which is also bounded from below by 1)
        wordlen   = len(words[0])
        wordcount = len(words)
        
        
        # step 2: iterate through s and get a dict where the keys are all starting indices and values are all words
        startsDict = dict()
        left = 0
        while left <= ( len(s) - wordlen ):
            candidate = s[left:(left+wordlen)]
            # print(left,candidate)
            if candidate in wordsDict:
                startsDict[left] = candidate
            left += 1
            
        # step 3: iterate through your keys
        # print(s[left:(left+wordlen)])
        # print(startsDict)
        res = []
        for start in startsDict:
            tempDict  = dict()
            for key in wordsDict:
                tempDict[key] = 0
            
            idx = start
            while idx in startsDict:
                key = startsDict[idx]
                tempDict[key] += 1
                # print(start,idx)
                # print(tempDict)
                # print(wordsDict)
                
                if tempDict == wordsDict:
                    res.append(start)
                    # print(res)
                    break
                elif tempDict[key] > wordsDict[key]:
                    # print( tempDict[key] > wordsDict[key] )
                    break
                
                idx += wordlen
            
                
        return res
		
# sliding window solution
# leverages the fact that all the words are the same size
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wlen   = len( words[0] )
        wcount = len(words)
        
        # make a dict
        wdict = dict()
        for w in words:
            if w in wdict:
                wdict[w] += 1
            else:
                wdict[w] = 1
        
        windowlen = wlen * wcount
        res = []
        """print(wdict)"""
        
        for left in range(wlen):
            currentleft = left
            while currentleft <= (len(s)-windowlen):
                """print('currentleft',currentleft,'endleft',len(s)-windowlen)
                print('res',res)"""
                tempdict = dict()
                for w in wdict:
                    tempdict[w] = wdict[w]
                lastlocs = dict()
                right = currentleft+wlen
                while right <= (currentleft + windowlen):
                    cword = s[(right-wlen):right]
                    """print(' ')
                    print('---')
                    print('tempdict',tempdict)
                    print('cword',cword)
                    print('lastlocs',lastlocs)"""
                    if cword in tempdict:
                        if tempdict[cword] > 0:
                            tempdict[cword] -= 1
                            if cword not in lastlocs:
                                lastlocs[cword] = right
                        else:
                            """print('excess',tempdict)"""
                            shiftleft = lastlocs[cword]
                            break
                    else:
                        shiftleft = right
                        break
                    right+=wlen
                
                if right > (currentleft+windowlen):
                    res.append(currentleft)
                    shiftleft = currentleft+wlen
                    
                currentleft = shiftleft
                """print(currentleft)
                print(' ')
                print('===')
                print('===')"""
                
        return res
                
            
            