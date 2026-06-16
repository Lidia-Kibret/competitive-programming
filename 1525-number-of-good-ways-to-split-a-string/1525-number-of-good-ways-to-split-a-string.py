class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right = Counter(s)

        ans = 0
        for ch in s[:-1]:
            left.add(ch)
            right[ch] -= 1
            if right[ch] == 0:
                del right[ch]
            if len(left) == len(right):
                ans += 1
        return ans


        