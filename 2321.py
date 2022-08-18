from heapq import *
class Solution:
    def smallestK(self, arr, k: int):
        smallheap=[]
        for i in arr:
            heappush(smallheap,i)
        return nsmallest(k,smallheap)
                
a=Solution()
print(a.smallestK([2,6,8,3,4,5,9,1],4))