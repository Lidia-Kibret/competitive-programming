class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = set()
        repeat = -1

        for num in nums:
            if num in res:
                repeat = num
            res.add(num)
            
        for i in range(1 , n + 1):
            if i not in res:
                missing = i
                break

        return [repeat, missing]
        