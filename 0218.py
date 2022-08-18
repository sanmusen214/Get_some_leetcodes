class Solution:
    def getSkyline(self, buildings):
        # 升序
        # 左端点右端点各自向左右找
        

a=Solution()
print(a.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
#[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]