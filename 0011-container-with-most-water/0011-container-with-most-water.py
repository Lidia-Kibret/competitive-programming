class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        Area = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            Area = max(Area , h * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return Area



        