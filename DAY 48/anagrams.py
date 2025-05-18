class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for word in arr:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
            
        return list(anagram_map.values())