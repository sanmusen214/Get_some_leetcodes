class Solution:
    def findBall(self, grid):
        row_len=len(grid)
        col_len=len(grid[0])
        #小球从side左-1上0右1滚到nownode,会从左-1下0右1出去,-2就是卡住
        def roll(nownode,side=0):
            if(grid[nownode[0]][nownode[1]]==1):#上转右，左转下
                if(side==0):
                    if(nownode[1]==col_len-1):
                        return -1
                    return 1
                elif(side==-1):
                    return 0
                else:
                    return -2
            else:#上转左，右转下，
                if(side==0):
                    if(nownode[1]==0):
                        return -2
                    return -1
                elif(side==1):
                    return 0
                else:
                    return -2

        result=[]
        for nowat in range(col_len):
            row_ind=0
            side=0
            haveresult=0
            while(row_ind<len(grid)):
                side=roll([row_ind,nowat],side)
                if(side==-2):
                    result.append(-1)
                    haveresult=1
                    break
                if(side==0):
                    side=0
                    row_ind+=1
                else:
                    nowat+=side
                    side=side*-1
            if(not haveresult):
                result.append(nowat)
        return result
                
            
            
                
                
a=Solution()
print(a.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(a.findBall([[-1]]))
