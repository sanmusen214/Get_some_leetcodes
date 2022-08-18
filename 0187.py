class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if(len(s)<10):
            return []
        else:
            table={}
            result=[]
            for i in range(10,len(s)+1):
                if(s[i-10:i] not in table):
                    table[s[i-10:i]]=1
                else:
                    table[s[i-10:i]]+=1
                    if(table[s[i-10:i]]==2):
                        result.append(s[i-10:i])
            return result
a=Solution()
print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
                    