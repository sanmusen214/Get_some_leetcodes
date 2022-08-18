# 从前往后累计求和差分数组的[0,j]的和即为j处结果数组的数值
# 区间增加时，i处+x，j+1处-x，为了确保可能发生的扩容的情况，如果差分数组长度不够，需要扩容
# 求结果数组时，需要给定一个限制的长度，少补多截。如果没有给限制长度，就根据是否发生扩容来考虑取len个还是len-1个（因为add如果扩容，end+1其实在结果数组中不存在
class Diff:
    # 初始化差分数组
    def __init__(self,lennum=0):
        # 这里lennum应当是 已知结果数组的长度的情况下的结果数组的长度
        self.nums=[0 for i in range(lennum)]
        # 是否发生扩容，如果发生扩容，后期返回默认数组长度就少一位
        self.extend=False
    # 区间增加，start,end为结果数组的下标，将【start，end】间所有数加number
    def add(self,start,end,number):
        # 如果差分数组长度不够，扩容，确保每个end+1都有减来确保后续add有数组扩容的情况
        if(end+1>len(self.nums)-1):
            self.extend=True
            self.nums+=[0 for i in range(end-len(self.nums)+2)]
        self.nums[start]+=number
        self.nums[end+1]-=number
    # 得到结果数组,数组限定length长度（短补长截
    # 如果给定length，严格按照长度。
    # 如果length为默认-1，如果相比于初始化的情况扩容了，则少最后一位。反之差分数组长度即为数值数组长度。
    def getresnums(self,length=-1):
        if(length==-1):
            if(self.extend):
                length=len(self.nums)-1
            else:
                length=len(self.nums)
        resnums=[]
        tsum=0
        for i in self.nums:
            tsum+=i
            resnums.append(tsum)
        if(len(resnums)<length):
            return resnums+[0 for i in range(length-len(resnums))]
        elif(len(resnums)>=length):
            return resnums[:length]
    # 得到差分数组
    def getdifnums(self):
        if(self.extend):
            return self.nums[:-1]
        return self.nums
    
df=Diff()
df.add(0,1,10)
df.add(1,2,20)
df.add(1,4,25)
print(df.getresnums(6))#[10,55,45,25,25]
print(df.getdifnums())
