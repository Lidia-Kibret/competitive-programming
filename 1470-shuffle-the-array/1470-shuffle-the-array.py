class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y = []
        for i in range(n):
            y.append(nums[i])
            y.append(nums[i + n])
        return y
        