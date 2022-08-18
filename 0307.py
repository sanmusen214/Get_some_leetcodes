class NumArray:
    def lowbit(self,num):
        return num&-num
    # 下标从1开始
    def __init__(self, nums: "List[int]"):
        prenum=[0]
        for each in nums:
            prenum.append(prenum[-1]+each)
        self.pnums=[0]#树状数组
        self.lennums=len(nums)#下标最右】
        for i in range(1,self.lennums+1):
            self.pnums.append(prenum[i]-prenum[i-self.lowbit(i)])
        self.ordnums=nums#原始数组
    def update(self, index: int, val: int) -> None:
        difval=val-self.ordnums[index]
        self.ordnums[index]=val
        index+=1
        while(index<=self.lennums):
            self.pnums[index]+=difval
            index=index+self.lowbit(index)
    def frontRange(self,index):
        total=0
        index+=1
        while(index>0):
            total+=self.pnums[index]
            index-=self.lowbit(index)
        return total
    def sumRange(self, left: int, right: int) -> int:
        return self.frontRange(right)-self.frontRange(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

a=NumArray([9,-8])
a.update(0,3)
print(a.sumRange(1,1))
print(a.sumRange(0,1))
a.update(1,-3)
print(a.sumRange(0,1))