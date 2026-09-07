class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            return 1

        nums.sort(key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"

        return "".join(nums)
        