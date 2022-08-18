class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            for c in range(i):
                if(nums[c]<nums[i]):
                    dp[i]=max(dp[i],dp[c]+1)
        return max(dp)

a=Solution()
print(a.lengthOfLIS([1,3,6,7,9,4,10,5,6]))#