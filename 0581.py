class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        numss=sorted(nums)
        start,end=-1,-2
        for i in range(len(nums)):
            if(numss[i]!=nums[i]):
                start=i
                break
        for i in range(len(nums)-1,-1,-1):
            if(numss[i]!=nums[i]):
                end=i
                break
        return end-start+1
    
        