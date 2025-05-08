class Solution:
    def matSearch(self, mat, x):
        if not mat or not mat[0]:
            return False
        
        n = len(mat)
        m = len(mat[0])
        
        i = 0       # start from the first row
        j = m - 1   # start from the last column
        
        while i < n and j >= 0:
            if mat[i][j] == x:
                return True
            elif mat[i][j] > x:
                j -= 1  # move left
            else:
                i += 1  # move down
        
        return False
