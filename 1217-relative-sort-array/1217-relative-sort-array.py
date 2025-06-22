class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for num in arr2:
            while num in arr1:
                result.append(num)     
                arr1.remove(num)
        arr1.sort()
        result += arr1
        return result 
        