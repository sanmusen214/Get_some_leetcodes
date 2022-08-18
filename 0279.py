class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float("inf") for i in range(n+1)]
        dp[0]=0
        square=[j**2 for j in range(1,100)]
        for i in range(1,n+1):
            for j in range(0,99):
                if(square[j]>i):break
                dp[i]=min(dp[i],dp[i-square[j]]+1)
        return dp[-1]
        
        
    
                
            
a=Solution()
print(a.numSquares(8441))
