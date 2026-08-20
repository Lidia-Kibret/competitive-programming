class Solution:

    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        result = ""

        while num > 0:
            result += str(num % 7)
            num //= 7

        if negative:
            result += "-"

        return result[::-1]