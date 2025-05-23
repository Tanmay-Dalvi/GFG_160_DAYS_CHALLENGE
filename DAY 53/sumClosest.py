class Solution:
    def sumClosest(self, arr, target):
        # code here
        if len(arr) < 2:
            return []
            
        arr.sort()
        left = 0
        right = len(arr) - 1
        
        closest_sum = float('inf')
        result_pair = []
        
        while left < right:
            a, b = arr[left], arr[right]
            curr_sum = a + b
            diff = abs(curr_sum - target)
            
            if diff < abs(closest_sum - target):
                closest_sum = curr_sum
                result_pair = [a, b]
            elif diff == abs(closest_sum - target):
                if abs(b - a) > abs(result_pair[1] - result_pair[0]):
                    result_pair = [a, b]
            
            if curr_sum < target:
                left += 1
            else:
                right -= 1
                
        return result_pair