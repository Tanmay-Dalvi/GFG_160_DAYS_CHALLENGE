class Solution:   
    def peakElement(self,arr):
        # Code here
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            left = arr[mid - 1] if mid - 1 >= 0 else float ('-inf')
            right = arr[mid + 1] if mid + 1 < len(arr) else float('-inf')
            
            if arr[mid] > left and arr[mid] > right:
                return mid
            elif arr[mid] < right:
                low = mid + 1
            else:
                high = mid - 1
        return -1