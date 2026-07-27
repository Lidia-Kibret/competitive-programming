class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            cou = target - nums[i]
            if cou in res:
                return[res[cou], i]
            res[nums[i]] = i

        