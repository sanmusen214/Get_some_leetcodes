import time
import bisect
# 1 2 3 4
# 1 4 3 4
# 差
class Solution:
    def minCost(self, grid: 'List[List[int]]') -> int:
        def legal(node):
            x=node[0]
            y=node[1]
            return x>=0 and x<len(grid) and y>=0 and y<len(grid[0])
        def dijstra(board,source,target=None):
            '''
            邻接矩阵放距离,-1无连接，对角默认-1，源点
            '''
            concern_his=[source] # 确定下来的顺序
            white={source:[0,source]} # 已确定的点， {自己：[距离源点总距离，上家]}
            gray=[] # 未确定但可到达的点 [[距离源点总距离，自己，上家],[距离源点总距离，自己，上家]] # 找最短距离，找某个点
            # 初始化gray
            for i in range(len(board[source])):
                if(board[source][i]!=-1):
                    bisect.insort(gray,[board[source][i],i,source])
            while(gray):
                # 弹出最短距离的gray点
                dis,me,father=gray.pop(0)
                if(me in white): #*每次新弹出之后判断被弹出点是否已确定（在white里即可，不区分新加点在不在grayset里，不用查找更新gray里某个点的距离数据
                    continue
                # 确定这个点放到white里
                white[me]=[dis,father]
                concern_his.append(me)
                # 如果这个就是目标点，直接结束
                if(target==me):
                    break
                # 更新与这个点相邻的点的距离,此处除了使用二维列表，也可以使用一个自定义的点对象来只用一维列表
                for nextnodeind in range(len(board[me])):
                    # 与ind点没有连结边，略过
                    if(board[me][nextnodeind]==-1):
                        continue
                    # ind（相邻点已经确定（在white中，略过
                    if(nextnodeind in white):
                        continue
                    # 从源点到刚确定下来的nextnodeind的距离=从原点到这个点的距离+这个点到nextnodeind的距离
                    newdis=white[me][0]+board[me][nextnodeind]
                    # 将这个点的信息排序插入gray列表
                    bisect.insort(gray,[newdis,nextnodeind,me])
            return {'history':concern_his,'result':white}
        tm=[(0,0),(0,1),(0,-1),(1,0),(-1,0)]
        xlen=len(grid)
        ylen=len(grid[0])
        pb=[[-1 for i in range(xlen*ylen)] for j in range(xlen*ylen)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val=grid[i][j]
                for p in range(len(tm)):
                    if(p==0):
                        continue
                    elif(p==val):
                        xx=i+tm[val][0]
                        yy=j+tm[val][1]
                        if(legal((xx,yy))):
                            pb[i*ylen+j][xx*ylen+yy]=0
                    else:
                        xx=i+tm[p][0]
                        yy=j+tm[p][1]
                        if(legal((xx,yy))):
                            # print(xx,yy)
                            pb[i*ylen+j][xx*ylen+yy]=1
        res=dijstra(pb,0,xlen*ylen-1)
        return res['result'][xlen*ylen-1][0]


                
                
            
a=Solution()
print(a.minCost([[3,4,3],[2,2,2],[2,1,1],[4,3,2],[2,1,4],[2,4,1],[3,3,3],[1,4,2],[2,2,1],[2,1,1],[3,3,1],[4,1,4],[2,1,4],[3,2,2],[3,3,1],[4,4,1],[1,2,2],[1,1,1],[1,3,4],[1,2,1],[2,2,4],[2,1,3],[1,2,1],[4,3,2],[3,3,4],[2,2,1],[3,4,3],[4,2,3],[4,4,4]]))