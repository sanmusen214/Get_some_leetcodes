class Solution:
    def highestPeak(self, isWater: "List[List[int]]") -> "List[List[int]]":
        len_rows=len(isWater)
        len_cols=len(isWater[0])
        board=[[-1 for i in range(len_cols)] for j in range(len_rows)]
        def fill_around(x,y,toWhich,thisround,board):
            check=0
            print(x,y,toWhich)
            if(x-1>=0 and board[x-1][y]==-1):
                board[x-1][y]=toWhich
                check=1
                thisround.append((x-1,y))
            if(x+1<=len_rows-1 and board[x+1][y]==-1):
                board[x+1][y]=toWhich
                check=1
                thisround.append((x+1,y))
            if(y-1>=0 and board[x][y-1]==-1):
                board[x][y-1]=toWhich
                check=1
                thisround.append((x,y-1))
            if(y+1<=len_cols-1 and board[x][y+1]==-1):
                board[x][y+1]=toWhich
                check=1
                thisround.append((x,y+1))
            print(board)
            if(check==1):
                return True
            else:
                return False
        #记录所有水
        lastround=list()
        for i in range(len_rows):
            for j in range(len_cols):
                if isWater[i][j]==1:
                    lastround.append((i,j))
                    board[i][j]=0
        #从水往外开始遍历
        times=1
        while(1):
            have_blank=0
            this_round=list()
            for w in lastround:
                if(fill_around(w[0],w[1],times,this_round,board)):
                    have_blank=1
            if(have_blank==0):
                break
            times+=1
            lastround=this_round
        return board
            
a=Solution()
print(a.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))
        