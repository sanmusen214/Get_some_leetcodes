class Solution:
    def maxSubArray(self, nums) -> int:
        dp=[0 for i in range(len(nums))]
        dp[0]=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
            m=max(m,dp[i])
        return m
                
                
a=Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
