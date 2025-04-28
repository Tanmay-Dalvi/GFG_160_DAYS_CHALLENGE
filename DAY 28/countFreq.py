class Solution:
    def countFreq(self, arr, target):
        #code here
        def binary_search_left(arr, target):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    result = mid
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result
            
        def binary_search_right(arr, target):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    result = mid
                    low = mid + 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result
            
        left = binary_search_left(arr, target)
        right = binary_search_right(arr, target)
        
        if left == -1:
            return 0
            
        return right - left + 1