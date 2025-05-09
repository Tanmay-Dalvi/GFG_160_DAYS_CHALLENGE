class Solution:
    
    # Function to search a given number in row-wise sorted matrix.
    def searchRowMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0

        for i in range(n):
            # Since each row is sorted, we can apply binary search on the row
            left, right = 0, m - 1
            while left <= right:
                mid = (left + right) // 2
                if mat[i][mid] == x:
                    return True
                elif mat[i][mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
