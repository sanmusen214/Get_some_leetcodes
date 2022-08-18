class Solution:
    def checkRecord(self, n: int) -> int:
        # set以元组作为键，超时
        # dp=[{} for i in range(n+1)]
        # (总共A，连续L)
        # dp[0][(0,0)]=1
        # countNum=0
        # blockNum=10**9+7
        # for i in range(1,n+1):
        #     if(i==n):
        #         for each in dp[i-1]:
        #             (A,L)=each
        #             number=dp[i-1][each]
        #             #拼接A
        #             if(A==0):#确保拼接后合格
        #                 countNum+=number
        #             #拼接L
        #             if(L<=1):#确保拼接后合格
        #                 countNum+=number
        #             #拼接P
        #             countNum+=number
        #         countNum%=blockNum
        #         break
        #     for each in dp[i-1]:
        #         (A,L)=each
        #         number=dp[i-1][each]
        #         #拼接A
        #         if(A==0):#确保拼接后合格
        #             if((A+1,0) not in dp[i]):
        #                 dp[i][(A+1,0)]=number
        #             else:
        #                 dp[i][(A+1,0)]+=number
        #         #拼接L
        #         if(L<=1):#确保拼接后合格
        #             if((A,L+1) not in dp[i]):
        #                 dp[i][(A,L+1)]=number
        #             else:
        #                 dp[i][(A,L+1)]+=number
        #         #拼接P
        #         if((A,0) not in dp[i]):
        #             dp[i][(A,0)]=number
        #         else:
        #             dp[i][(A,0)]+=number
        # return countNum
        
        # 总共A，连续L，dp值代表数量
        # +A,+L,+P
        # 注意L要是连续
        #0: A=0,L=0
        #1: A=0,L=1
        #2: A=0,L=2
        #3: A=1,L=0
        #4: A=1,L=1
        #5: A=1,L=2
        dp=[[0 for j in range(6)] for i in range(n+1)]
        dp[0][0]=1
        mod=10**9+7
        for i in range(1,n+1):
            dp[i][0]=(0+0+(dp[i-1][0]+dp[i-1][1]+dp[i-1][2]))%mod
            dp[i][1]=(0+dp[i-1][0]+0)%mod
            dp[i][2]=(0+dp[i-1][1]+0)%mod
            dp[i][3]=((dp[i-1][0]+dp[i-1][1]+dp[i-1][2])+0+(dp[i-1][3]+dp[i-1][4]+dp[i-1][5]))%mod
            dp[i][4]=(0+dp[i-1][3]+0)%mod
            dp[i][5]=(0+dp[i-1][4]+0)%mod
        return (sum(dp[n]))%mod
a=Solution()
print(a.checkRecord(100000))

            