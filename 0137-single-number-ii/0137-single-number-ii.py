class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0

        for bit in range(32):
            count = 0

            for num in nums:
                if (num >> bit) & 1:
                    count += 1

            if count % 3:
                answer |= (1 << bit)

     
        if answer >= 2**31:
            answer -= 2**32

        return answer
        