class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        ps = 0
        pm = {0: 1}

        for num in nums:
            ps += num

            if(ps - k) in pm:
                c += pm[ps - k]

            pm[ps] = pm.get(ps, 0) + 1
        return c

        