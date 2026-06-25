class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in res:
                res.remove(s[left])
                left += 1
            
            res.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len        