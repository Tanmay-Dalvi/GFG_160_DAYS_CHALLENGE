class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        
        n = len(arr)
        
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                correct_idx = arr[i] - 1
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
                
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
                
        return n + 1