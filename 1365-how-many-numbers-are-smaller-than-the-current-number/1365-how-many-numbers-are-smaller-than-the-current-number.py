class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        y = []
        for num in nums:
            y.append(sorted_nums.index(num))
        return y

        