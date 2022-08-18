class Solution:
    def threeSum(self, nums):
        if(len(nums)<3):
            return []
        nums.sort()
        for i in nums:
            if(nums.count(i)>3):
                nums=nums[:nums.index(i)]+nums[(nums.index(i)+nums.count(i)-3):]
        left=0
        center=1
        right=len(nums)-1
        result=[]
        tru=1
        right_to_left=1 #控制right指针是否往左移
        while(tru==1):  #三个指针，left，center从左，right从右
            if(left==len(nums)-2):  #left到最右头
                break
            if(center==len(nums)-1):
                left+=1
                center=left+1
                right=len(nums)-1
                right_to_left=1
                continue
            if(right==center): #right碰到center
                center+=1
                right=center+1
                right_to_left=0
                continue
            if(right==len(nums)): #right到最右边
                right_to_left=1
                center+=1
                right=len(nums)-1
                continue
            if(center==len(nums)-1 or -nums[left]<2*nums[center]):#剩余数字将会出现在center的左边-->left和center和过大，本次循环over，left+=1
                left+=1
                center=left+1
                right=len(nums)-1
                right_to_left=1
                continue
            if(nums[left]+nums[center]+nums[right]<0): #right显小，center继续移动
                center+=1
                right_to_left=1
                continue
            if(-nums[center]<2*nums[left]): #剩余数字将会出现在left的左边-->left和center和过大，上一个if排除了center的问题，这一个是left的问题，则无剩余解
                break
            if(nums[left]+nums[center]+nums[right]==0): #如果为0，判断填入
                c=max(nums[left],nums[center],nums[right])
                a=min(nums[left],nums[center],nums[right])
                b=-a-c
                if(not [a,b,c] in result):
                    result.append([a,b,c])
                center+=1 #填入后center需要往右移一
                if(right==center):
                    left+=1
                    center=left+1
                    right=len(nums)-1
                    right_to_left=1
                    continue
                right_to_left=1 #因为center变大继续现有right往左
                right+=1
            if(right_to_left==1):
                right-=1
            else:
                right+=1
        return result
                
            
         
                    
a=Solution()
# print(a.threeSum([3,0,-2,-1,1,2]))
# print(a.threeSum([-1,0,1,2,-1,-4]))
# print(a.threeSum([4,0,2,3,-1]))
print(a.threeSum([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(a.threeSum([1,-1,-1,0]))

