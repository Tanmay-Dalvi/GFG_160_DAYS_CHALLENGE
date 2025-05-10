class Solution:
    
    # Function to search a given number in strictly sorted matrix.
    def searchMatrix(self, mat, x):
        if not mat or not mat[0]:
            return False
        
        n = len(mat)
        m = len(mat[0])
        
        low = 0
        high = n * m - 1
        
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            mid_value = mat[row][col]
            
            if mid_value == x:
                return True
            elif mid_value < x:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
