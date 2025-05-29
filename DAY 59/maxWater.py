class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        if n <= 2:
            return 0
            
        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        trapped_water = 0
        
        while left < right:
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                    
                else:
                    trapped_water += left_max - arr[left]
                left += 1
                
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    trapped_water += right_max - arr[right]
                right -= 1
                
        return trapped_water