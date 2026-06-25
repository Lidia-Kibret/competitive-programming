class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price

            else:
                max_price = max(max_price, price - min_price)
        return max_price 
        