class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = set(nums)
        count = 0
        for num in result:
            if num - 1 not in result:
                current_num = num
                length = 1

                while current_num + 1 in result:
                    current_num += 1
                    length += 1
                
                count = max(count, length)
        return count
        

        