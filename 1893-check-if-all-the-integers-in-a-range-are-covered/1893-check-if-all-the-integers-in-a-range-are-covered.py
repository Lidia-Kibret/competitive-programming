class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

         my_set = set()
        
         for start, end in ranges:
            for num in range(start, end + 1):
                my_set.add(num)
        
         for num in range(left, right + 1):
            if num not in my_set:
                return False
        
         return True
        