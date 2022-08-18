class Solution:
    def isValidSudoku(self, board) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    continue
                if(show_times_in_col(board,col,board[row][col])==1 and show_times_in_row(board,row,board[row][col])==1):
                    y=int(col/3)+1
                    x=int(row/3)+1
                    if(show_times_in_square(board,y,x,board[row][col])!=1):
                        return False
                else:
                    return False
        return True


# 检查99宫格第col列数字wantnum出现次数，返回int
def show_times_in_col(alist,col,wantnum):
    showtime=0
    for times in range(9):
        if(alist[times][col]==wantnum):
            showtime+=1
    return showtime

# 检查99宫格第row行数字wantnum出现次数，返回int
def show_times_in_row(alist,row,wantnum):
    showtime=0
    for times in range(9):
        if(alist[row][times]==wantnum):
            showtime+=1
    return showtime

# 检查99宫格第squarenum块数字wantnum出现次数,x(1,2,3),y(1,2,3)
def show_times_in_square(alist,squarenumy,squarenumx,wantnum):
    showtime=0
    for j in range(squarenumy*3-3,squarenumy*3):
        for i in range(squarenumx*3-3,squarenumx*3):
            if(alist[i][j]==wantnum):
                showtime+=1
    return showtime
            
            
            

a=Solution()
sodoku=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(a.isValidSudoku(sodoku))

