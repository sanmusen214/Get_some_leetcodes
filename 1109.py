# class Solution:
#     # 差分 对于一个区间内整体增加一个值v操作，在区间起始点+=v，在区间结束点-=v消除影响。最后求每个点最终结果时，求前缀和（含）即可，如果在有效区间内则只受+=v影响，如果只是包含某些有效区间，+-v互相抵消
#     def corpFlightBookings(self, bookings, n: int):
#         chalist=[0 for i in range(n+1)]
#         for eachbk in bookings:
#             l=eachbk[0]-1
#             r=eachbk[1]
#             num=eachbk[2]
#             chalist[l]+=num
#             chalist[r]-=num
#         #输出答案
#         tempsum=0
#         results=[]
#         for i in range(len(chalist)-1):
#             tempsum+=chalist[i]
#             results.append(tempsum)
#         return results
class Diff:
    def __init__(self,len=1000):
        self.nums=[0 for i in range(len)]
    def add(self,start,end,number):
        self.nums[start]+=number
        if(end+1<=len(self.nums)-1):
            self.nums[end+1]-=number
    def getindex(self,index):
        return self.nums[index]
    def getresnums(self):
        resnums=[]
        tsum=0
        for i in self.nums:
            tsum+=i
            resnums.append(tsum)
        return resnums
    def get(self,index):
        res=0
        for i in range(index+1):
            res+=self.nums[index]
        return res
class Solution:
    def corpFlightBookings(self, bookings, n: int):
        diff=Diff(n)
        for each in bookings:
            diff.add(each[0]-1,each[1]-1,each[2])
        return diff.getresnums()      
                
a=Solution()
print(a.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5))