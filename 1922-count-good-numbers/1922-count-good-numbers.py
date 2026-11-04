class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = 10**9 + 7

        even = (n + 1) // 2
        odd = n // 2

        a = pow(5, even, mod)
        b = pow(4, odd, mod)

        return (a * b) % mod