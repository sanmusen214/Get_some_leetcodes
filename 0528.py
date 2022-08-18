import random
from bisect import bisect_left
class Solution:
    
    def __init__(self, w):
        # [5,14,1,7]
        # [5,19,20,27]
        self.presum=[]
        tempsum=0
        for i in w:
            tempsum+=i
            self.presum.append(tempsum)
        self.totalsum=tempsum
        

    def pickIndex(self) -> int:
        randnum=random.random()*self.totalsum
        p = bisect_left(self.presum, randnum)
        return p
            
    
a=Solution([5,14,1,7])
results=[]
testtimes=5000
for i in range(testtimes):
    results.append(a.pickIndex())
for index in range(4):
    print("%d have %f probs"%(index,results.count(index)/testtimes))