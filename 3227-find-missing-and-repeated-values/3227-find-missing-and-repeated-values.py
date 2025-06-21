class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
         nums = [num for row in grid for num in row]
         n = len(grid)
         total = n * n

         for i in range(1, total + 1):
            if nums.count(i) == 2:
                a = i
            elif nums.count(i) == 0:
                b = i

         return [a, b]
        