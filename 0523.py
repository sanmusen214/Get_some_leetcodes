class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        #计算前缀和，看似是滑块n方，其实只要n次顺序计算目前的余数，记录余数，两相同余数之间的和余数为0
        #记录之前n个数的和余数，用到的是set,计算效率高于list
        yulist={0}
        #存储上一个，前缀和和之间只代表一个数，题目需要至少两个数组成的滑块
        #当前
        now=nums[0]%k
        for i in range(1,len(nums)):
            
            #更新前缀和
            ready,now=now,(now+nums[i])%k
            if(now in yulist):
                return True
            yulist.add(ready)
        return False
                
                    
a=Solution()
print(a.checkSubarraySum([23,2,6,4,7],13))
