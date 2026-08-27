class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        length = 0
        has_odd = False

        for freq in count.values():
            length += (freq // 2) * 2

            if freq % 2 == 1:
                has_odd = True

        if has_odd:
            length += 1

        return length
        