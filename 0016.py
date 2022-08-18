class Solution:
    def threeSumClosest(self, nums,target):
        mindif=abs(nums[0]+nums[1]+nums[2]-target)
        mindif_total=nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in nums:
            if(nums.count(i)>3):
                nums=nums[:nums.index(i)]+nums[(nums.index(i)+nums.count(i)-3):]
        for left in range(len(nums)-2): 
            if(nums[left]+nums[left+1]+nums[left+2]>mindif_total and abs(nums[left]+nums[left+1]+nums[left+2]-target)>mindif):
                break
            for center in range(left,len(nums)-1):
                if(center==left):
                    continue
                if(nums[left]+nums[center]>target): #left,center大于target,right从小往大逼近
                    lastdif=abs(nums[left]+nums[center]+nums[center+1]-target) #记录第一次right的lastdif
                    for right in range(center,len(nums)):
                        if(right==center):
                            continue
                        if(abs(nums[left]+nums[center]+nums[right]-target)<mindif):
                            mindif=abs(nums[left]+nums[center]+nums[right]-target)
                            mindif_total=nums[left]+nums[center]+nums[right]
                            lastdif=abs(nums[left]+nums[center]+nums[right]-target)
                            continue
                        if(abs(nums[left]+nums[center]+nums[right]-target)>lastdif): #距离target变远
                            break
                        lastdif=abs(nums[left]+nums[center]+nums[right]-target)
                else: #left和center小于target，right从大往小逼近
                    lastdif=abs(nums[left]+nums[center]+nums[len(nums)-1]-target)
                    for right in range(len(nums)-1,center,-1):
                        if(abs(nums[left]+nums[center]+nums[right]-target)<mindif):
                            mindif=abs(nums[left]+nums[center]+nums[right]-target)
                            mindif_total=nums[left]+nums[center]+nums[right]
                            lastdif=abs(nums[left]+nums[center]+nums[right]-target)
                            continue
                        if(abs(nums[left]+nums[center]+nums[right]-target)>lastdif): #距离target变远
                            break
                        lastdif=abs(nums[left]+nums[center]+nums[right]-target)
        return mindif_total
                    
    


s=Solution()
print(s.threeSumClosest([1,1,1,0],-100)) #2
print(s.threeSumClosest([0,2,1,-3],1)) #0
print(s.threeSumClosest([-1,0,1,1,55],3)) #2
print(s.threeSumClosest([1,2,5,10,11],12))  #13
print(s.threeSumClosest([1,2,4,8,16,32,64,128],82))  #82
