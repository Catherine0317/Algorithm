class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        d.sort(key = lambda x:(-len(x),x))
    
        for word in d:
            p1 = 0
            for character in s:
                if p1 < len(word) and word[p1] == character:
                    p1 += 1
                if p1 == len(word):
                    return word 
        return ""
