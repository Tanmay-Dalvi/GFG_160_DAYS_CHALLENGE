class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        stalls.sort()
        
        def canPlaceCows(min_dist):
            count = 1
            last_pos = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = stalls[i]
                    if count == k:
                        return True
            return False
            
        low = 1
        high = stalls[-1] - stalls[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result