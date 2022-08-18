class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #先转置，后对称，一次旋转4个像素并标记，下次就不用转他们了
        len_m=len(matrix)
        markmatrix=[[0 for j in range(len(matrix))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if(markmatrix[i][j]==1):
                    continue
                matrix[j][len_m-1-i],matrix[len_m-1-i][len_m-1-j],matrix[len_m-1-j][i],matrix[i][j]=matrix[i][j],matrix[j][len_m-1-i],matrix[len_m-1-i][len_m-1-j],matrix[len_m-1-j][i]
                markmatrix[i][j]=1
                markmatrix[j][len_m-1-i]=1
                markmatrix[len_m-1-i][len_m-1-j]=1
                markmatrix[len_m-1-j][i]=1

                        
            

            
            
a=Solution()
mat=[[1,2,3],[4,5,6],[7,8,9]]
a.rotate(mat)
print(mat)
        