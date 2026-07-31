class Solution:
    def summaryRanges(self, nums):
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            end = nums[i]

            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{end}")

            i += 1

        return ans
        