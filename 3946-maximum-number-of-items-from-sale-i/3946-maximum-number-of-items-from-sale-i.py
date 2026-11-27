
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        min_price = min(item[1] for item in items)

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            factor = items[i][0]
            price = items[i][1]

            free = 0

            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    free += 1

            value = 1 + free

            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    dp[c] = max(dp[c], dp[c - price] + value)

        ans = 0

        for c in range(budget + 1):
            if dp[c] != -1:
                remaining = budget - c
                total = dp[c] + remaining // min_price
                ans = max(ans, total)

        return ans
