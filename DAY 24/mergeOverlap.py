class Solution:
    def mergeOverlap(self, arr):
        # Step 1: Sort the intervals based on the start time
        arr.sort(key=lambda x: x[0])

        merged = []
        for interval in arr:
            # If merged is empty or there is no overlap with the last interval, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap found, merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
