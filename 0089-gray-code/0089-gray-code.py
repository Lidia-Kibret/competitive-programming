class Solution:
    def grayCode(self, n: int) -> list[int]:

        result = []

        for i in range(1 << n):
            result.append(i ^ (i >> 1))

        return result