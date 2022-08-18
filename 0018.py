class Solution:
    def fourSum(self, nums, target):
        if(len(nums)<4):
            return []
        nums.sort()
        numlist=[]
        for a in range(0,len(nums)-3):
            for b in range(a,len(nums)-2):
                if(b==a):
                    continue
                for c in range(b,len(nums)-1):
                    if(c==b):
                        continue
                    if (target-nums[a]-nums[b]-nums[c] in nums[c+1:] and not [nums[a],nums[b],nums[c],target-nums[a]-nums[b]-nums[c]] in numlist):
                        numlist.append(list([nums[a],nums[b],nums[c],target-nums[a]-nums[b]-nums[c]]))
        return numlist
        
            
a=Solution()
# print(a.fourSum([1,0,-1,0,-2,2],0))
print(a.fourSum([-2,-1,-1,1,1,2,2],0))
