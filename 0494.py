class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        # 初始化需要注意正数一个，负数一个，0和-0属于同一数字，因此挨个添加第二个
        tempset={nums[0]:1}
        if(-nums[0] in tempset):
            tempset[-nums[0]]+=1
        else:
            tempset[-nums[0]]=1
        # 记录当前数字加减后，各种和的数量，2^n
        for i in nums[1:]:
            newset={}
            for each in tempset:
                if each+i in newset:
                    newset[each+i]+=tempset[each]
                else:
                    newset[each+i]=tempset[each]
                if each-i in newset:
                    newset[each-i]+=tempset[each] 
                else:
                    newset[each-i]=tempset[each]
            tempset=newset
            # print(tempset)
        if(target in tempset):
            return tempset[target]
        return 0
        
a=Solution()
print(a.findTargetSumWays([0,0,0,0,0,0,0,0,1],1))
print(a.findTargetSumWays([1,1,1,1,1],3))
