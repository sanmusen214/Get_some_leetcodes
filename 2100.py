class Solution:
    def goodDaysToRobBank(self, security, time: int):
        #得到左边右边最大非递增情况
        dp=[[0,0] for i in range(len(security))]
        for i in range(1,len(security)):
            if(security[i]-security[i-1]<=0):
                dp[i][0]=dp[i-1][0]+1
            if(security[len(security)-i-1]-security[len(security)-i]<=0):
                dp[len(security)-i-1][1]=dp[len(security)-i][1]+1
        return [e for e in range(len(security)) if dp[e][0]>=time and dp[e][1]>=time]

a=Solution()
print(a.goodDaysToRobBank([5,3,3,3,5,6,2],2))
print(a.goodDaysToRobBank([1,1,1,1,1,1,1,1],2))
print(a.goodDaysToRobBank([5],2))

