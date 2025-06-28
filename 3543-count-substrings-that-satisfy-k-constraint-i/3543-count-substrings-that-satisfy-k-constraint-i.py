class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
         n = len(s)
         result = 0
 
         for i in range(n):
            zeros = 0
            ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    zeros += 1
                else:
                    ones += 1
            
                if zeros <= k or ones <= k:
                    result += 1
                else:
                    break

         return result
        