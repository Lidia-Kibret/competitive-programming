class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        total = 0
        for i in nums:
            total += i
            ans.append(total)
        return ans
        