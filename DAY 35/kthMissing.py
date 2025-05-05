class Solution:
    def kthMissing(self, arr, k):
        # code here
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return left + k