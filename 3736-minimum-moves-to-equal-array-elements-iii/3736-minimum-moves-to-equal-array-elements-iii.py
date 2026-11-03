class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)

        total_moves = 0

        for i in range(len(nums)):
            total_moves += maximum - nums[i]

        return total_moves