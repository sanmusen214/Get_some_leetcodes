class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        dpmatrix=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        def dp():
            for x in range(len(matrix)):
                for y in range(len(matrix[0])):
                    if(x==0 and y==0):
                        dpmatrix[x][y]=matrix[x][y]
                    elif(x==0):
                        dpmatrix[x][y]=dpmatrix[x][y-1]^matrix[x][y]
                    elif(y==0):
                        dpmatrix[x][y]=dpmatrix[x-1][y]^matrix[x][y]
                    else:
                        dpmatrix[x][y]=dpmatrix[x-1][y]^dpmatrix[x][y-1]^dpmatrix[x-1][y-1]^matrix[x][y]
        dp()
        ml=[dpmatrix[r][i] for i in range(len(dpmatrix[0])) for r in range(len(dpmatrix))]
        ml.sort()
        return ml[-k]
        
        
a=Solution()
print(a.kthLargestValue([[5,2],[1,6]],4))
