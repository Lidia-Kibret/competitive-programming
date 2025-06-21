class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr =  {}
        for i in range(len(nums)):
            lid = target - nums[i]
            if lid in arr:
                return[arr[lid] ,i]
            arr[nums[i]] =i