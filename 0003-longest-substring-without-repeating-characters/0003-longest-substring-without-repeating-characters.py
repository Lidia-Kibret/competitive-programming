class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        empty_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            
            while s[right] in empty_set:
                empty_set.remove(s[left])
                left += 1
            empty_set.add(s[right])
            max_len = max(max_len , right - left + 1)
        return max_len
                
        