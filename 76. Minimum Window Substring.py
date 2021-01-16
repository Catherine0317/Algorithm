from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        dict_t = Counter(t)
        l,r = 0,0
        count = len(t)
        min_length = len(s)+1
        output = ""
        
        while r < len(s):
            if s[r] in dict_t:
                if dict_t[s[r]] > 0:
                    count -= 1
                dict_t[s[r]] -= 1
            while count == 0:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    output = s[l:r+1]
                if s[l] in dict_t:
                    dict_t[s[l]] += 1
                    if dict_t[s[l]] > 0:
                        count += 1
                l += 1
            r += 1
        return output
