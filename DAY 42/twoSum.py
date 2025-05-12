class Solution:
    def twoSum(self, arr, target):
        value_to_index = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in value_to_index:
                return True  # You found two distinct indices
            value_to_index[num] = i  # Store index of the current number
        return False
