class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        right = 0
        while right < len(s):
            if right - left + 1 < 3:
                right += 1
            elif right - left + 1 == 3:
                window = s[left:right + 1]
                if len(set(window)) == 3:
                    count += 1
                left += 1
                right -1
        return count 
        