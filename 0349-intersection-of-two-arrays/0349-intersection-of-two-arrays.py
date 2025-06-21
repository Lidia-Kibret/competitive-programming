class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [] 
        set1 = set(nums1)
        set2 = set(nums2)

        for num in set1:
            if num in set2:
                result.append(num)

        return result