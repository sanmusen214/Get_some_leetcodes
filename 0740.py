# class Solution:
#     def deleteAndEarn(self, nums) -> int:
#         unnum=list(set(nums))
#         # 合并相同数
#         timelist=[each*nums.count(each) for each in unnum]
#         dp=[0 for i in range(len(timelist))]
#         if(len(timelist)<=1):
#             return timelist[0]
#         # 初始化
#         dp[-1]=timelist[-1]
#         if(abs(unnum[-1]-unnum[-2])==1):            #互斥
#             dp[-2]=max(timelist[-1],timelist[-2])
#         else:                                       #不互斥
#             dp[-2]=timelist[-1]+timelist[-2]
#         # dp
#         for i in range(len(timelist)-3,-1,-1):
#             if(abs(unnum[i]-unnum[i+1])==1):        #互斥
#                 dp[i]=max(timelist[i]+dp[i+2],dp[i+1])
#             else:                                   #不互斥
#                 dp[i]=timelist[i]+dp[i+1]
#         return dp[0]
                
class Solution:
    def deleteAndEarn(self, nums) -> int:
        unnum=list(set(nums))
        # 合并相同数(timelist[i]=set(nums[i])*出现次数）
        timelist=[unnum[0]*nums.count(unnum[0])]
        for p in range(1,len(unnum)):               #*不互斥的之间塞个0转为不互斥
            if abs(unnum[p]-unnum[p-1])!=1:
                timelist.append(0)
            timelist.append(unnum[p]*nums.count(unnum[p]))
        dp=[0 for i in range(len(timelist))]
        if(len(timelist)==1):
            return timelist[0]
        # 初始化
        dp[-1]=timelist[-1]
        dp[-2]=max(timelist[-1],timelist[-2])
        # dp
        for i in range(len(timelist)-3,-1,-1):
            dp[i]=max(timelist[i]+dp[i+2],dp[i+1])#互斥

        return dp[0]

                

a=Solution()
print(a.deleteAndEarn([2,2,3,3,3,4]))
print(a.deleteAndEarn([3,4,2]))
print(a.deleteAndEarn([3,1]))
print(a.deleteAndEarn([1,1,1,1,1,1,1,1,2,3,4,4,4,5,6]))
