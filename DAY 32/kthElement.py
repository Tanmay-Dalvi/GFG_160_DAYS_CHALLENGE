class Solution:

    def kthElement(self, a, b, k):
        i, j = 0, 0
        while True:
            if i == len(a):
                return b[j + k - 1]
            if j == len(b):
                return a[i + k - 1]
            if k == 1:
                return min(a[i], b[j])
                
            mid = k//2
            new_i = min(i + mid, len(a)) - 1
            new_j = min(j + mid, len(b)) - 1
            if a[new_i] < b[new_j]:
                k -= new_i - i + 1
                i = new_i + 1
            else:
                k -= new_j - j + 1
                j = new_j + 1