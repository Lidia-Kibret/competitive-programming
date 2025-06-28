class Solution:
    def longestNiceSubstring(self, s: str) -> str:
         n = len(s)

         for size in range(n, 1, -1):  
            for i in range(n - size + 1):  
                sub = s[i:i + size]
                letters = set(sub)

                if all(c.swapcase() in letters for c in letters):
                    return sub  

         return ""
        