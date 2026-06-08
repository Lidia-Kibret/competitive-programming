class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for key, value in enumerate(s):
            if freq[value] == 1:
                return key
        return -1

        