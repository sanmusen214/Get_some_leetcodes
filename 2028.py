class Solution:
    def missingRolls(self, rolls: "List[int]", mean: int, n: int) -> "List[int]":
        totaln=mean*(len(rolls)+n)-sum(rolls)
        if(totaln<n or totaln>6*n):
            return []
        totaln-=n
        result=[1 for i in range(n)]
        index=-1
        for i in range(5,0,-1):
            while(totaln!=0):
                index+=1
                if(totaln-i>0):
                    result[index]+=i
                    totaln-=i
                elif(totaln-i==0):
                    result[index]+=i
                    totaln-=i
                    return result
                elif(totaln-i<0):
                    index-=1
                    break
        return result
    
a=Solution()
print(a.missingRolls([6,1,6,2,4,4,5],5,16))
