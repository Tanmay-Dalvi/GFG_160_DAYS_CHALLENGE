class Solution:
    def findMin(self, arr):
        #complete the function here
        lo, hi = 0, len(arr) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid
                
        return arr[lo]