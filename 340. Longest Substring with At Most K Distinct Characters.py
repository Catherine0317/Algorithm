from collections import Counter 
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        max_length = 0
        left = 0
        cnt = Counter()
        
        for i, c in enumerate(s):
            cnt[c] += 1
            
            while len(cnt) > k:
                cnt[s[left]] -= 1
                
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
                
            max_length = max(max_length,i-left+1)
        return max_length
        
        
        
                    
            
    
