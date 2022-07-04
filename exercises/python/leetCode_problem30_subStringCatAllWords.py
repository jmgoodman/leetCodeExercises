class Solution:
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
            