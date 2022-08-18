class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countDict=dict()
        countSet=set()
        for i in t:
            countDict[i]=countDict.get(i,0)+1
            countSet.add(i)
        lp=0
        rp=0
        while(rp<len(s)):
            if(s[rp] in countSet):
                countDict[s[rp]]=countDict[s[rp]]-1
                if(countDict[s[rp]]==0):
                    countDict.pop(s[rp])
                if(len(countDict.keys())==0):
                    while(1):
                        if(s[lp] in countSet):
                            countDict[s[lp]]=countDict[s[rp]]+1
                            if(countDict[s[]])
                            break
                            
                        lp+=1
                rp+=1
        

### PPAPPPBCABC    P

