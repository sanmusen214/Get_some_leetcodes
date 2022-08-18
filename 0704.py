class Solution:
    def search(self, nums, target: int) -> int:
        left=-1
        right=len(nums)
        while(left+1!=right):
            center=int((left+right)/2)
            if(center==target):
                return center
            if(center>target):
                right=center
            else:
                left=center
            print(left,right)
        return -1
        
a=Solution()
print(a.search( [-1,0,3,5,9,12],9))