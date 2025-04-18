class Solution:
    def search(self, pat, txt):
        # code here
        def computeLPSArray(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
            
        m = len(pat)
        n = len(txt)
        lps = computeLPSArray(pat)
            
        result = []
        i = 0
        j = 0
        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            if j == m:
                result.append(i - j)
                j = lps[j - 1]
            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                        i +=1
                        
        return result