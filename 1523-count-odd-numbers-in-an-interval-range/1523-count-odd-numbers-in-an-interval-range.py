class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high + 1) // 2 - (low) // 2
        return ans
    

        