class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result


        