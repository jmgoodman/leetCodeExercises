class Codec: # this is gonna need a database. presumably a hash table whose memory addresses map cleanly and invertibly to shortened URLs
    def __init__(self):
        self.hashmap = dict() # no need to implement everything by hand...

    def genKeyNum(self, longUrl:str) -> int:
        runningSum  = 0
        maxN        = 50
        N           = min(maxN,len(longUrl))
        nChar       = 3
        nCharSchatz = 62
        period      = nCharSchatz**nChar
        for idx in range(N):
            runningSum =  ( runningSum + ord(longUrl[-(idx+1)]) ) % int(period)

        return runningSum

    def genKeyStr(self,keyNum:int) -> str:
        _keyNum = keyNum
        nChar   = 3
        nCharSchatz = 62
        outStr = ''
        for idx in range(nChar):
            pd = nCharSchatz**(nChar-idx-1)
            charNum = _keyNum // pd
            _keyNum -= charNum * pd
            outStr += self.convert2char(charNum)

        return outStr

    def genKey(self, longUrl:str) -> (str,int):
        keyNum = self.genKeyNum(longUrl)
        keyStr = self.genKeyStr(keyNum)
        return (keyStr,keyNum)

    def convert2char(self,charNum:int)->str:
        if charNum >= 52:
            return chr(charNum-52+48)
        elif charNum >= 26:
            return chr(charNum-26+97)
        else:
            return chr(charNum+65)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        (keyStr,keyNum) = self.genKey(longUrl)
        while keyStr in self.hashmap: # collision handling: seek thru the table til you find a free slot
            # you SHOULD check if this URL is already stored though
            if self.hashmap[keyStr] != longUrl:
                keyNum = (keyNum+1) % int(62**3)
                keyStr = self.genKeyStr(keyNum)
            else:
                return 'https://tinyurl.com/'+keyStr

        self.hashmap[keyStr] = longUrl
        return 'https://tinyurl.com/'+keyStr
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        keyStr = shortUrl[-3:] # last 3 chars
        return self.hashmap[keyStr] # no need to handle collisions, the URL they're given is the one you look up!
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))