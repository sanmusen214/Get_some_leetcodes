class Solution:
    def search(self, nums, target: int) -> int:
        if(len(nums)==1):
            if(nums[0]==target):
                return 0
            else:
                return -1
        if(target>=nums[0]):
            for i in range(len(nums)):
                if(nums[i]==target):
                    return i
                if(i==len(nums)-1 or nums[i+1]<nums[i]):
                    return -1
        else:
            for i in range(len(nums)-1,-1,-1):
                if(nums[i]==target):
                    return i
                if(i==0 or nums[i-1]>nums[i]):
                    return -1
            
            
            

a=Solution()
print(a.search([1,3],0))

