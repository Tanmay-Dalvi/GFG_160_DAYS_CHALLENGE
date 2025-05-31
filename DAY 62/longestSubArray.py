class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum_map = {}
        current_sum = 0
        max_length = 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            if current_sum == k:
                max_length = i + 1
                
            if (current_sum - k) in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[current_sum - k])
                
            if current_sum not in prefix_sum_map:
                prefix_sum_map[current_sum] = i
            
        return max_lengthS