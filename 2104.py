class Solution:
    def subArrayRanges(self, nums) -> int:
        total=0
        #定义dp，存储从前到后的最小，最大值
        for l in range(len(nums)):
            for r in range(l,len(nums)):
                if(r==l):#初始化dp
                    lastblock=[nums[r],nums[r]]
                else:
                    # print(dp[l])
                    # print(l,r)
                    # 维护
                    lastblock=[min(lastblock[0],nums[r]),max(lastblock[1],nums[r])]
                    total+=(lastblock[1]-lastblock[0])
        return total

a=Solution()
print(a.subArrayRanges([1,2,3]))
                