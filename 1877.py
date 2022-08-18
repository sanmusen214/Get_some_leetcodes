class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        maxm=float("0")
        for i in range(int(len(nums)/2)):
            maxm=max(nums[i]+nums[-1-i],maxm)
        return maxm
        
a=Solution()
print(a.minPairSum([3,5,4,2,4,6]))
        
        
        
                