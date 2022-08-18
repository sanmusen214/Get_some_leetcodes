class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]<=0):
                nums=nums[i+1:]
                break
        if(len(nums)==0 or min(nums)!=1):
            return 1
        else:
            for i in range(1,len(nums)):
                if(nums[i]==nums[i-1]+1 or nums[i]==nums[i-1]):
                    continue
                else:
                    return nums[i-1]+1
            return nums[-1]+1
                    




a=Solution()
print(a.firstMissingPositive([0,2,2,1,1]))
