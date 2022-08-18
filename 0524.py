class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:
        mayresult=[]
        maxlen=0
        for each in dictionary:
            pd=0
            for ptr in range(len(s)):
                if(s[ptr]==each[pd]):
                    pd+=1
                if(pd==len(each)):
                    mayresult.append(each)
                    maxlen=max(maxlen,len(each))
                    break
        return sorted([each for each in mayresult if len(each)==maxlen])[0] if mayresult else ""
    
a=Solution()
print(a.findLongestWord("apple",["zxc","vbn"]))
