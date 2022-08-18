class Solution:
    def missingNumber(self, nums) -> int:
        allnums=set()
        for i in range(len(nums)+1):
            allnums.add(i)
        for e in nums:
            allnums.remove(e)
        return allnums.pop()

a=Solution()
print(a.missingNumber([9,6,4,2,3,5,7,0,1]))