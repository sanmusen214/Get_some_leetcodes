items=[[2,3],[3,4],[4,5],[5,6]]
maxweight=5
dp=[[0 for w in range(maxweight+1)] for i in range(len(items)+1)]

for i in range(1,len(items)+1):         #*物体可选范围逐渐增大，不拿物体时dp为0
    for w in range(1,maxweight+1):      #*限重逐渐增大，可能有重量为0的物体，所以可以选择考虑下标0
        wi=items[i-1][0]                #物体下标比dp表里少一
        vi=items[i-1][1]                #物体下标比dp表里少一
        if wi<=w:                       #*物体可以单独放下当前限重
            if vi+dp[i-1][w-wi]>dp[i-1][w]:#*拿取当前物品+剩余空间剩余物品的最大dp>不拿取当前物品的最大dp，拿
                dp[i][w]=vi+dp[i-1][w-wi]
            else:                       #*反之不拿
                dp[i][w]=dp[i-1][w]
        else:                           #*压根拿不了，不拿
            dp[i][w]=dp[i-1][w]
print(dp)
        