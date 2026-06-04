class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)
            if len(s) < 3:
                return 0
            
            count = 0
            for i in range(1, len(s) -1):
                left = s[i - 1]
                mid = s[i]
                right = s[i + 1]

                if mid > left and mid > right:
                    count += 1
                elif mid < left and mid < right:
                    count += 1
            return count

        total = 0
        for num in range(num1, num2 + 1):
            total += waviness(num)
        return total
        
        