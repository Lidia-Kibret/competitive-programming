class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            count = target - nums[i]
            if count in seen:
                return[seen[count], i]
            seen[nums[i]] = i

        