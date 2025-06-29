class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []            
        current_sum = 0        
        for num in nums:
            current_sum += num 
            prefix.append(current_sum) 
        return prefix
        