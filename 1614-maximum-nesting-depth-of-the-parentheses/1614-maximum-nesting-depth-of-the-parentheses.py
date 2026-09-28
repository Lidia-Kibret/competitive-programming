class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0

        for i in s:
            if i == '(':
                count += 1
                ans = max(ans, count)

            elif i == ')':
                count -= 1

        return ans