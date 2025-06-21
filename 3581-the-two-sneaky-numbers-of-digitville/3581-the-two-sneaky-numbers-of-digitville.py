class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x = set()
        dup = []
    
        for num in nums:
            if num in x:
                dup.append(num)
            else:
                x.add(num)
    
        return dup
        