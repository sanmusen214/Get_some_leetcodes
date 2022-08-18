class Solution:
    def largestNumber(self, nums) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if(int(str(nums[j+1])+str(nums[j]))>int(str(nums[j])+str(nums[j+1]))):  #！str（后者+前者）大于str（前者+后者）
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        if(sum(nums)==0):
            return "0"
        strnums=[str(i) for i in nums]
        return ''.join(strnums)
                    

#返回使排列数字最大的组合（动态规划）
a=Solution()
print(a.largestNumber([3,30,34,5,9]))#9 5 34 3 30
print(a.largestNumber([432,43243]))#43243 432
print(a.largestNumber([111311,1113]))#1113 111311
