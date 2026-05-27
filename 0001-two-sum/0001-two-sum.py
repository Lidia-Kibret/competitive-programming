class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in result:
                return[result[complement] ,i]

            result[nums[i]] = i

        