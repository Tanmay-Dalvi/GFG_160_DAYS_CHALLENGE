class Solution:
    
    #Function to find minimum number of pages.
    def isPossible(self, arr, k, max_pages):
        student_count = 1
        pages_sum = 0
        
        for pages in arr:
            if pages > max_pages:
                return False
                
            if pages_sum + pages > max_pages:
                student_count += 1
                pages_sum = pages
                if student_count > k:
                    return False
            else:
                pages_sum += pages
                
        return True
    
    def findPages(self, arr, k):
        #code here
        if k > len(arr):
            return -1
            
        low = max(arr)
        high = sum(arr)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.isPossible(arr, k, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result