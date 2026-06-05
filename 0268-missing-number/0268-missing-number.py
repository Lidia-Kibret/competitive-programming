class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total = n / 2 * (1 + n)
        current = sum(nums)
        return int(total - current)

        