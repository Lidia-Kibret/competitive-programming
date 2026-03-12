class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i in range(len(nums)):
            count = target - nums[i]

            if count in result:
                return [result[count], i]

            result[nums[i]] = i
            
            
        