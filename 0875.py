import math
import time


class Solution:
    def minEatingSpeed(self, piles: 'List[int]', h: int) -> int:
        piles.sort()
        if(h==len(piles)):
            return piles[-1]
        def computeSpeed(k):
            totalhour=0
            for p in piles:
                if(p<=k):
                    totalhour+=1
                else:
                    totalhour+=math.ceil(p/k)
            return totalhour
        tempk=0
        delta=0
        while(1):
            temptime=computeSpeed(tempk+2**delta)
            print("speed: ",tempk+2**delta,", time:",temptime,", delta: ",delta)
            if(temptime>h):
                delta=max(delta*2,1)
            elif(temptime<=h and delta==0):
                return tempk+2**delta
            elif(temptime<=h):
                delta=int(delta/2)
                tempk=tempk+2**delta
                delta=0
                
a=Solution()
print(a.minEatingSpeed([30,11,23,4,20],6))
print(a.minEatingSpeed([312884470],312884469))
