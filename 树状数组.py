class NumArray:
    # 二进制数的最低位1
    def lowbit(self,num):
        return num&-num
    #用数组初始化
    def __init__(self, nums: "List[int]"):
        #构建前缀和数组
        prenum=[0]
        for each in nums:
            prenum.append(prenum[-1]+each)
        #构建树状数组
        self.pnums=[0]#有效下标从1开始
        self.lennums=len(nums)#树状数组的最大有效下标】
        for i in range(1,self.lennums+1):
            self.pnums.append(prenum[i]-prenum[i-self.lowbit(i)])
        self.ordnums=nums#原始数组
    def update(self, index: int, val: int) -> None:
        #通过原数组得出新老数的差值
        difval=val-self.ordnums[index]
        self.ordnums[index]=val
        index+=1#原数组下标转换为树状数组下标
        while(index<=self.lennums):
            #由左下到右上，依次给节点值修正差值，加上lowbit即可得到自己的父母节点位置
            self.pnums[index]+=difval
            index=index+self.lowbit(index)
    def frontRange(self,index):
        #求原数组【0，index】的和
        total=0
        index+=1#原数组下标转换为树状数组下标
        while(index>0):
            #由右下到左上，减去lowbit即可得到自己的邻近左兄弟节点位置
            #如果自己是最左兄弟，则可得到父母/祖父母的邻近左兄弟节点位置
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