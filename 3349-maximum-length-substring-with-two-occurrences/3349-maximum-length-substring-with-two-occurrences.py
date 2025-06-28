class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1

            while char_count[char] > 2:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
            current_substring = s[left:right+1]
            max_len = max(max_len, len(current_substring))
        return max_len
        