class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.listm=[]
        # 0为偶，1为奇


    def addNum(self, num: int) -> None:
        if(len(self.listm)!=0):
            for i in range(len(self.listm)):
                if(self.listm[i]>num):
                    self.listm.insert(i,num)
                    return
        self.listm.append(num)
            

    def findMedian(self) -> float:
        return self.listm[int(len(self.listm)/2)] if len(self.listm)%2==1 else (self.listm[int(len(self.listm)/2)]+self.listm[int(len(self.listm)/2)-1])/2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(6)
obj.addNum(4)
obj.addNum(8)
param_2 = obj.findMedian()
print(param_2)
