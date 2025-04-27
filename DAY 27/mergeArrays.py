class Solution:
    def mergeArrays(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        
        def nextGap(gap):
            if gap <= 1:
                return 0
            return (gap // 2) + (gap % 2)
            
        gap = nextGap(n + m)
        
        while gap > 0 :
            i = 0
            while i + gap < n:
                if a[i] > a[i + gap]:
                    a[i], a[i + gap] = a[i + gap], a[i]
                i += 1
                
            j = gap - n if gap > n else 0
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
                    
            if j < m:
                j = 0
                while j + gap < m:
                    if b[j] > b[j + gap]:
                        b[j], b[j + gap] = b[j + gap], b[j]
                    j += 1
                    