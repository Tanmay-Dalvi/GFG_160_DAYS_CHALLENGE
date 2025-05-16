class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        union_set = set(a)
        union_set.update(b)
        return len(union_set)