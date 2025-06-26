class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place = 0
        for seek in range(len(nums)):
            if nums[seek] != 0:
                nums[place] , nums[seek] = nums[seek] , nums[place]
                place +=1        