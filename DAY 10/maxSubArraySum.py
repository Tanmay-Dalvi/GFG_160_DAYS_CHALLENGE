class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        max_current = max_global = arr[0]
        
        for i in range (1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            max_global = max(max_global, max_current)
            
        return max_global