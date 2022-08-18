class Solution:
    def numEnclaves(self, grid) -> int:
        w=len(grid)
        n=len(grid[0])
        def startround(x,y):
            grid[x][y]=2
            if(x-1>0 and grid[x-1][y]==1):
                startround(x-1,y)
            if(y-1>0 and grid[x][y-1]==1):
                startround(x,y-1)
            if(x+1<w and grid[x+1][y]==1):
                startround(x+1,y)
            if(y+1<n and grid[x][y+1]==1):
                startround(x,y+1)
                
        for i in range(w):
            if(grid[i][0]==1):
                startround(i,0)
            if(grid[i][n-1]==1):
                startround(i,n-1)
        for i in range(n):
            if(grid[0][i]==1):
                startround(0,i)
            if(grid[w-1][i]==1):
                startround(w-1,i)
        return sum([line.count(1) for line in grid])
a=Solution()
print(a.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]))