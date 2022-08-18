class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1=len(word1)
        len_2=len(word2)
        dp={}
        for i in range(-1,len_1):
            for j in range(-1,len_2):
                if(i==-1 or j==-1):
                    dp[(i,j)]=0
                elif(word1[i]==word2[j]):
                    dp[(i,j)]=dp[(i-1,j-1)]+1
                else:
                    dp[(i,j)]=max(dp[(i-1,j)],dp[(i,j-1)])
        return len_1+len_2-2*dp[(len_1-1,len_2-1)]
    
a=Solution()
print(a.minDistance("sea","eat"))