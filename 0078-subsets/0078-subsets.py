class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, subset):
            res.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res
        