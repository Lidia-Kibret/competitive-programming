class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * (max(costs) + 1)

        for c in costs:
            freq[c] += 1

        ans = 0

        for cost in range(1, len(freq)):
            if coins < cost:
                break

            buy = min(freq[cost], coins // cost)
            ans += buy
            coins -= buy * cost

        return ans