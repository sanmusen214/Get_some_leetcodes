class Solution:
    def numIslands(self, grid) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    grid=span_one_point(grid,i,j)
                    count+=1
        return count
            


def span_one_point(mappic,rowp,colp):
    mappic[rowp][colp]="2"
    if(rowp-1>=0 and mappic[rowp-1][colp]=="1"):
        mappic = span_one_point(mappic,rowp-1,colp)
    if(colp+1<=len(mappic[0])-1 and mappic[rowp][colp+1]=="1"):
        mappic = span_one_point(mappic,rowp,colp+1)
    if(rowp+1<=len(mappic)-1 and mappic[rowp+1][colp]=="1"):
        mappic = span_one_point(mappic,rowp+1,colp)
    if(colp-1>=0 and mappic[rowp][colp-1]=="1"):
        mappic = span_one_point(mappic,rowp,colp-1)
    return mappic
    
    

a=Solution()
grid=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(a.numIslands(grid))

