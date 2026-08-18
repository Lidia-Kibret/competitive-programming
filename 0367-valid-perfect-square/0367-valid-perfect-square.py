class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2

            if mid == num // mid and num % mid == 0:
                return True

            if mid < num // mid:
                left = mid + 1
            else:
                right = mid - 1

        return False
        