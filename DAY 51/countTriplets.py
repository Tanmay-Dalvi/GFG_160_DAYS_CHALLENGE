class Solution:
    def countTriplets(self, arr, target):
        # code here
        n = len(arr)
        count = 0
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total == target:
                    if arr[left] == arr[right]:
                        num_elements = right - left + 1
                        count += num_elements * (num_elements - 1) // 2
                        break
                    else:
                        left_count = 1
                        right_count = 1
                        while left + 1 < right and arr[left] == arr[left + 1]:
                            left += 1
                            left_count += 1
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            right -= 1
                            right_count += 1
                        count += left_count * right_count
                        left += 1
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return count