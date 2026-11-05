class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)

        table = [[0] * n for i in range(n)]

        for i in range(n):
            table[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                left = nums[i] - table[i + 1][j]
                right = nums[j] - table[i][j - 1]

                table[i][j] = max(left, right)

        return table[0][n - 1] >= 0