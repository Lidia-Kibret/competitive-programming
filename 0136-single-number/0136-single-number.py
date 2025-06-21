class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            if count == 1:
                return num
        