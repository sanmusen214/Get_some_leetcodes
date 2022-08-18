class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if(maxMove==0):
            return 0
        def trythis(nowRow,nowCol,steps):
            ret=[]
            for i in range(-1,2,2):
                ret.append([nowRow+i,nowCol,steps-1])
                ret.append([nowRow,nowCol+i,steps-1])
            return ret
        trylist=[{} for i in range(maxMove+1)]
        trylist[maxMove][(startRow,startColumn)]=1
        count=0
        blocknum=10**9+7
        for i in range(maxMove,0,-1):#循环dp
            # print([k for k in trylist[i]])
            # print(count)
            for p in trylist[i]:#循环每个有值的位置
                temp=trythis(p[0],p[1],i)
                for each in temp:#对于接下来的四个位置
                    if(min(m-each[0]-1,each[0],n-each[1]-1,each[1])<0):#出界，count加上现在dp格子里的值
                        count+=trylist[i][(p[0],p[1])]
                        count%=blocknum
                    elif(each[2]!=0):#未出界，加入下次dp
                        if((each[0],each[1]) not in trylist[each[2]]):
                            trylist[each[2]][(each[0],each[1])]=trylist[i][(p[0],p[1])]
                        else:
                            trylist[each[2]][(each[0],each[1])]+=trylist[i][(p[0],p[1])]
        return count
        

a=Solution()
print(a.findPaths(1,3,3,0,1))