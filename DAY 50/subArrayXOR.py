class Solution:
    def subarrayXor(self, arr, k):
        # code here
        from collections import defaultdict
        
        xor_count = defaultdict(int)
        count = 0
        prefix_xor = 0
        
        for num in arr:
            prefix_xor ^= num
            
            if prefix_xor == k:
                count += 1
                
            count += xor_count[prefix_xor ^ k]
            
            xor_count[prefix_xor] += 1
            
        return count