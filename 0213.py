class Solution:
    def rob(self, nums) -> int:
        if(len(nums)<=3):
            return max(nums)
        if(len(nums)==4):
            return max(nums[0]+nums[2],nums[1]+nums[3])
        else:
            def robfirsec(start,now,money):  #将金额传递
                if(now==len(nums)+1 and start==0):
                    return money-nums[-1]
                if(now>len(nums)-1 or (now==len(nums)-1 and start==0)):
                    return money
                if(now==len(nums)-1 and start!=0):
                    return money+nums[-1]
                money1=money+nums[now] #偷目前第一个
                money2=money+nums[now+1] #偷目前第二个
                return max((robfirsec(start,now+2,money1),robfirsec(start,now+3,money2)))
            return max(robfirsec(0,2,nums[0]),robfirsec(1,3,nums[1]),robfirsec(2,4,nums[2])) #初始的房子一定偷
                    

            
            
            
            





a=Solution()
# print(a.rob([0]))
# print(a.rob([1,7,9,4])) #11
# print(a.rob([4,1,2,7,5,3,1]))#14
print(a.rob([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]))#2926
print(a.rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) #16
print(a.rob([155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]))#4388
