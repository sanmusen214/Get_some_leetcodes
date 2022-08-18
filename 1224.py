class Solution:
    def maxEqualFreq(self, nums) -> int:
        countnum=dict()#记录次数对应数字set
        numscount=dict()#记录数字对应的次数
        maxres=0
        for i in range(len(nums)):
            # 更新table
            lastcount=numscount.get(nums[i],0)
            numscount[nums[i]]=lastcount+1

            lastset=countnum.get(lastcount,set())
            if(nums[i] in lastset):
                lastset.remove(nums[i])
            if(lastset):
                countnum[lastcount]=lastset
            else:
                countnum.pop(lastcount,0)
            nextset=countnum.get(lastcount+1,set())
            nextset.add(nums[i])
            countnum[lastcount+1]=nextset
            # print(countnum,numscount)
            # 判断是否
            if(len(countnum.keys())==1):
                onecount=max(countnum.keys())
                if(onecount==1 or len(countnum[onecount])==1):
                    maxres=i+1
            if(len(countnum.keys())==2):
                biggercount=max(countnum.keys())
                smallercount=min(countnum.keys())
                if(len(countnum[biggercount])==1 and biggercount==smallercount+1):
                    maxres=i+1
                if(len(countnum[smallercount])==1 and smallercount==1):
                    maxres=i+1
        return maxres
   
a=Solution()
print(a.maxEqualFreq( [1,1,1,2,2,2,3,3,3]))#7
print(a.maxEqualFreq([1,2]))#2
print(a.maxEqualFreq([2,2,1,1,5,3,3,5]))#7
print(a.maxEqualFreq([1,1]))#2
print(a.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))#13
