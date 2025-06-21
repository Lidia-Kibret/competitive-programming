class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        majority_count = len(nums) // 2
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > majority_count:
                return num