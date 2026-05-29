class Solution:
    def minElement(self, nums):
        min_value = float('inf')

        for num in nums:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10

            if total < min_value:
                min_value = total

        return min_value