class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in result:
                return True
            result[num] = True
           
        return False
        