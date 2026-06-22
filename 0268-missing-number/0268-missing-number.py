class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = set(nums)
        for i in range(len(nums) + 1):
            if i not in res:
                return i
        