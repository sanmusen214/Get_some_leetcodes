class Solution:
    def change(self, amount, coins):
        if(coins[0]>amount):return 0
        dp=[[] for i in range(amount+1)]
        dp[coins[0]]=[[coins[0]]]
        for m in range(coins[0]+1,amount+1):
            for c in coins:
                if(m-c<coins[0] and m!=c):break
                if(m==c):
                    dp[m].append([c])
                    break
                for temp in dp[m-c]:
                    each=temp.copy()
                    each.append(c)
                    each.sort()
                    if(each not in dp[m]):
                        dp[m].append(each)
        # print(dp)
        return len(dp[-1])
        
    
                
            
a=Solution()
print(a.change(5,[1,2,5]))
