class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = set()
        for num in nums:
            if num in x:
                return True
            x.add(num)
        return False