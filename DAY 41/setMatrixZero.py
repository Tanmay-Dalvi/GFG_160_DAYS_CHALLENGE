class Solution:
    def setMatrixZeroes(self, mat):
        first_row_zero = any(mat[0][j] == 0 for j in range(len(mat[0])))
        first_col_zero = any(mat[i][0] == 0 for i in range(len(mat)))
        
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
                    
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
                    
        if first_row_zero:
            for j in range(len(mat[0])):
                mat[0][j] = 0
                
        if first_col_zero:
            for i in range(len(mat)):
                mat[i][0] = 0