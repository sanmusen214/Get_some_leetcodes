"""
# Definition for a QuadTree node.
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        # x轴方向的前n个的前缀和，判断区域是否相同直接区间求面积，如果为0或等于应该有的面机，则区域内东西相同
        sumx=[]
        for eachline in grid:
            thissumx=[0]
            for each in eachline:
                thissumx.append(thissumx[-1]+each)
            sumx.append(thissumx)
        # 判断区域是否相同
        def judgeSame(x1,x2,y1,y2):
            x1,x2=min(x1,x2),max(x1,x2)
            y1,y2=min(y1,y2),max(y1,y2)
            total=0
            for y in range(y1,y2+1):
                total+=(sumx[y][x2+1]-sumx[y][x1])
            if(total==0):
                # 全是0
                return 0
            elif(total==(y2-y1+1)*(x2-x1+1)):
                # 全是1
                return 1
            # 完全不同，-8而不是-1，防止1,1,-1,-1
            return -8
        # 得到节点,[x1,x2]
        def getNode(x1,x2,y1,y2):
            if(x1==x2 and y1==y2):
                return Node(grid[y1][x2],True,None,None,None,None)
            x1,x2,y1,y2=min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2)
            xhalf,yhalf=int((x2-x1)/2),int((y2-y1)/2)
            # 四个子区域是否各自相同
            stateLT=judgeSame(x1,x1+xhalf,y1,y1+yhalf)
            stateRT=judgeSame(x1+xhalf+1,x2,y1,y1+yhalf)
            stateLB=judgeSame(x1,x1+xhalf,y1+yhalf+1,y2)
            stateRB=judgeSame(x1+xhalf+1,x2,y1+yhalf+1,y2)
            sumstate=stateLT + stateRT + stateLB + stateRB
            if sumstate == 0:
                return Node(False,True,None,None,None,None)
            elif sumstate == 4:
                return Node(True,True,None,None,None,None)
            else:
                return Node(True,False,
                            getNode(x1,x1+xhalf,y1,y1+yhalf),
                            getNode(x1+xhalf+1,x2,y1,y1+yhalf),
                            getNode(x1,x1+xhalf,y1+yhalf+1,y2),
                            getNode(x1+xhalf+1,x2,y1+yhalf+1,y2))
        return getNode(0,len(grid[0])-1,0,len(grid[0])-1)
    
a=Solution()
print(a.construct([[1,0,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]))

        
            