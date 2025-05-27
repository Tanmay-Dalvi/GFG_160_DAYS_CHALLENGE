class Solution:
    def countDistinct(self, arr, k):
        from collections import defaultdict

        if k > len(arr):
            return []

        freq_map = defaultdict(int)
        result = []

        # First window
        for i in range(k):
            freq_map[arr[i]] += 1
        result.append(len(freq_map))

        # Remaining windows
        for i in range(k, len(arr)):
            # Remove the element going out of the window
            outgoing = arr[i - k]
            freq_map[outgoing] -= 1
            if freq_map[outgoing] == 0:
                del freq_map[outgoing]

            # Add the new element coming into the window
            incoming = arr[i]
            freq_map[incoming] += 1

            result.append(len(freq_map))

        return result
