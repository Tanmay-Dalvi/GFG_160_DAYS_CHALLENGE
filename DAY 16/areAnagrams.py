class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1) != len(s2):
            return False
            
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1
            
        for ch in s2:
            freq2[ord(ch) - ord('a')] += 1
            
        return freq1 == freq2