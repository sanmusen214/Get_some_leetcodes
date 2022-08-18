class Solution:
    def numberOfArithmeticSlices(self, nums: "List[int]") -> int:
        # dp=[[0,0],[0,0]]
        # if(len(nums)<3):
        #     return 0
        # else:
        #     for times in range(2,len(nums)):
        #         arilist=[nums[i]-nums[i-1] for i in range(times-1,times)]
        #         if(arilist[0]==arilist[1]):
        #             dp.append([nums[times],arilist[0]])
        #         for each in dp[times-1]:
        count=0
        def isSlice(left,right):
            #包括左右边界
            cha=nums[left+1]-nums[left]
            chalist=[nums[i]-nums[i-1] for i in range(left+1,right+1)]
            if(chalist.count(cha)==len(chalist)):
                return [True,cha]
            else:
                return [False,-1]
        if(len(nums)<3):return 0
        for i in range(len(nums)-2):
            cha=isSlice(i,i+2)
            # print(cha)
            if(cha[0]):
                for j in range(i+2,len(nums)):
                    print(nums[j]-nums[j-1])
                    if(nums[j]-nums[j-1]==cha[1]):
                        count+=1
                        # print("answer add {},{}".format(i,j))
                    else:
                        break
        return count
            
a=Solution()
print(a.numberOfArithmeticSlices([1,2,3,8,9,10]))