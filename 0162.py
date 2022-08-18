class Solution:
    def findPeakElement(self, nums) -> int:
        def ispeak(index):
            if(index==0):
                if nums[index]>nums[index+1]:
                    return 0
                else:
                    return 1
            if(index==len(nums)-1):
                if nums[index]>nums[index-1]:
                    return 0
                else:
                    return -1
            if(nums[index]>nums[index+1] and nums[index-1]<nums[index]):
                return 0
            if(nums[index]<nums[index+1] and nums[index-1]<nums[index]):
                return 1
            if(nums[index]>nums[index+1] and nums[index-1]>nums[index]):
                return -1
            else:
                return 1
        if(len(nums)==1):
            return 0
        start=int(len(nums)/2)
        left=-1
        right=len(nums)
        while(right-left!=2):
            center=int((left+right)/2)
            if(nums[center]>nums[center+1]):
                right=center+1
            else:
                left=center
        return int((left+right)/2)
                
a=Solution()
print(a.findPeakElement([1,2]))
print(a.findPeakElement([1,2,3,4,5,6,4,3,1,2]))

print(a.findPeakElement([3,1,2]))