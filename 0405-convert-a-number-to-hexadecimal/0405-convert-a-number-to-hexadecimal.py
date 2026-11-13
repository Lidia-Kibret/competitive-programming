class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        num = num & 0xffffffff

        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num = num // 16

        return result