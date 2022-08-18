class Solution:
    def numberOfBoomerangs(self, points) -> int:
        # 字典存储每个点距离其他点的距离，相同的距离计数，后续使用这些相同距离的数量两两组合（n（n-1））
        table=[{} for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dis=pow((points[i][0]-points[j][0]),2)+pow((points[i][1]-points[j][1]),2)
                if(dis not in table[i]):
                    table[i][dis]=1
                else:
                    table[i][dis]+=1
                if(dis not in table[j]):
                    table[j][dis]=1
                else:
                    table[j][dis]+=1
        # print(table)
        results=0
        for line in table:
            for eachdis in line:
                if(line[eachdis]>=2):
                    results+=(line[eachdis]*(line[eachdis]-1))
        return results
                
            
a=Solution()
print(a.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
