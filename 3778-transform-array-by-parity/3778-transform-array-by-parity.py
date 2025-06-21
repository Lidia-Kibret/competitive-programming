class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] % 2 == 0 else 1
        nums.sort()
        return nums
        