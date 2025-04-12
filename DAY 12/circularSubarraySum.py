def circularSubarraySum(arr):
    ##Your code here
    def kadane(nums):
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        return max_global
        
    max_kadane = kadane(arr)
    
    total_sum = sum(arr)
    
    inverted_arr = [-x for x in arr]
    max_inverse_kadane = kadane(inverted_arr)
    
    max_wrap = total_sum + max_inverse_kadane
    
    if max_wrap == 0:
        return max_kadane
    else:
        return max(max_kadane, max_wrap)