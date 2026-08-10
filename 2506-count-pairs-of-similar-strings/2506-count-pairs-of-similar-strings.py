class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = {}
        ans = 0

        for word in words:
            key = frozenset(word)

            if key in count:
                ans += count[key]

            count[key] = count.get(key, 0) + 1

        return ans
        