class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        left = 0
        right = t - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n
            
            mid_num = matrix[i][j]

            if mid_num == target:
                return True
            elif mid_num < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        