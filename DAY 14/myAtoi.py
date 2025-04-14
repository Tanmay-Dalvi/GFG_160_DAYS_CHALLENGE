class Solution:
    def myAtoi(self, s):
        # Code here
        int_max = 2**31 - 1
        int_min = -2**31
        
        i = 0
        n = len(s)
        result = 0
        sign = 1
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
            
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            
            if result > (int_max - digit) // 10:
                return int_max if sign == 1 else int_min
                
            result = result * 10 + digit
            i += 1
            
        return sign * result