class Solution:
    def jump(self, nums) -> int:
        dp=[0 for i in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<=len(nums)-i-1):
                addnum=min(dp[i+1:i+1+nums[i]]) if nums[i]!=0 else float("inf")
            else:
                addnum=min(dp[i+1:])
            dp[i]=addnum+1
        return dp[0]
            
    

                

a=Solution()
print(a.jump([2,3,1,1,4]))
