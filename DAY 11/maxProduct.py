class Solution:

    # Function to find maximum product subarray
    def maxProduct(self, arr):
        if not arr:
            return 0

        max_ending_here = arr[0]
        min_ending_here = arr[0]
        max_so_far = arr[0]

        for i in range(1, len(arr)):
            temp = max_ending_here  # Save max before updating

            max_ending_here = max(arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here)
            min_ending_here = min(arr[i], arr[i] * temp, arr[i] * min_ending_here)

            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
