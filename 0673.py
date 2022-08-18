class Solution:
    def findNumberOfLIS(self, nums) -> int:
        longest=1
        count=1
        dp=[1 for i in range(len(nums))]
        dptimes=[0 for i in range(len(nums))]
        dptimes[0]=1
        for i in range(1,len(nums)):
            thiscount=1
            for c in range(i):
                # 如果可以添加
                if(nums[c]<nums[i]):
                    #添加后比原先的dp[i]大
                    if(dp[c]+1>dp[i]):
                        dp[i]=dp[c]+1
                        thiscount=dptimes[c]
                    #添加后和原先dp[i]一样
                    elif(dp[c]+1==dp[i]):
                        thiscount+=dptimes[c]
                    #添加后比全局longest长
                    if(dp[c]+1>longest):
                        longest=dp[c]+1
                        count=dptimes[c]
                    #添加后和全局longest一样长
                    elif(dp[c]+1==longest):
                        count+=dptimes[c]
            dptimes[i]=thiscount
            #dp[i]只能自己开头
            if(dp[i]==1):
                dptimes[i]=1
                #和全局longest一样长
                if(dp[i]==longest):
                    count+=dptimes[i]
        return count

a=Solution()
print(a.findNumberOfLIS([2,2,2,2,2]))#5
print(a.findNumberOfLIS([1,3,5,4]))#2
print(a.findNumberOfLIS([1,2,4,3,5,4,7,2]))#3
print(a.findNumberOfLIS([3,1,2]))#1
print(a.findNumberOfLIS([1,2,3,1,2,3,1,2,3]))#10
print(a.findNumberOfLIS([2,5,5,7,8,9]))#2

def change(listm):
    for each in listm:
        print(each+50,end=",")
# change([-52,-28,-28,-11,-6,-20,-32,-36,1])