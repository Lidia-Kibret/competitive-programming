class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        total = 0
        for i in range(len(s)):
            val = s[i]
            num = pairs[s[i]]

            if i < len(s) - 1 and num < pairs[s[i + 1]]:
                total -= num
            else:
                total += num
        return total 
                