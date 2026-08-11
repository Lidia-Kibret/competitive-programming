class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = "0"
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                ans = max(ans, num[i : i + 3])
        return "" if ans == "0" else ans

        