class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = []
        for i in nums:
            rank.append(sorted_nums.index(i))
        return rank 
        