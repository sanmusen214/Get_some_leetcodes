class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def insect(p1l,p1r,p2l,p2r):
            if(p2l<p1l):
                if(p2r<p1l):
                    return 0
                elif(p2r>=p1l and p2r<=p1r):
                    return p2r-p1l
                elif(p2r>p1r):
                    return p1r-p1l
            elif(p2l>=p1l and p2l<=p1r):
                if(p2r>=p1l and p2r<=p1r):
                    return p2r-p2l
                elif(p2r>p1r):
                    return p1r-p2l
            elif(p2l>=p1r):
                return 0
        return insect(ax1,ax2,ax1,ax2)*insect(ay1,ay2,ay1,ay2)+insect(bx1,bx2,bx1,bx2)*insect(by1,by2,by1,by2)-insect(ax1,ax2,bx1,bx2)*insect(by1,by2,ay1,ay2)
    
a=Solution()  
print(a.computeArea(-3,0,3,4,0,-1,9,2))