class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        
        while x != 0:
            digit = int(x % 10)
            
            if x < 0 and digit > 0:
                digit -= 10
            
         
            if rev > 214748364 or (rev == 214748364 and digit > 7):
                return 0
            if rev < -214748364 or (rev == -214748364 and digit < -8):
                return 0
            
            rev = rev * 10 + digit
            x = (x - digit) // 10
        
        return rev
        