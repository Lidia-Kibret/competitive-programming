class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        res = []
        for num in nums:
            res.append(sorted_nums.index(num))
        return res

        