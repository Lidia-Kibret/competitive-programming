class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            count = target - nums[i]
            if count in res:
                return[res[count], i]
            res[nums[i]] = i

        