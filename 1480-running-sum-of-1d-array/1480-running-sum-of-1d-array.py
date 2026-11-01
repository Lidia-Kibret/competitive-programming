class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        total = 0
        for i in nums:
            total += i
            res.append(total)
        return res
        