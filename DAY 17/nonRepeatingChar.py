class Solution:
    def nonRepeatingChar(self,s):
        #code here
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in s:
            if count[char] == 1:
                return char
                
        return '$'