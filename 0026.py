class Solution:
    def removeDuplicates(self, nums):
        ptr=0
        for i in range(len(nums)):
            if(i==0):
                ptr+=1
                continue
            if(nums[i]==nums[i-1]):
                continue
            if(nums[i]!=nums[i-1]):
                nums[ptr]=nums[i]
                ptr+=1
        return ptr
                
            
                

                


                
            
a=Solution()
print(a.removeDuplicates([0,0,1,1,2,3,3,4,5,5,6,7,7]))
