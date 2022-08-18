class Solution:
    def splitArray(self, nums, m: int) -> int:
        def compute(cap):
            count=0
            tempc=0
            for num in nums:
                tempc+=num
                if(tempc>cap):
                    count+=1
                    tempc=num
            if(tempc>0):
                count+=1
            return count
        left=max(nums)
        right=sum(nums)
        while(left<right):
            mid=left+int((right-left)/2)
            if(compute(mid)==m):
                right=mid
            elif(compute(mid)<m):
                right=mid
            elif(compute(mid)>m):
                left=mid+1
        return left
    
a=Solution()
print(a.splitArray([7,2,5,10,8],2))