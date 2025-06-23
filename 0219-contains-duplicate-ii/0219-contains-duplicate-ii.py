class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lid = {}
        for i , num in enumerate(nums):
            if num in lid and i - lid[num] <= k:
                return True
            lid[num] = i
        return False 
        
        