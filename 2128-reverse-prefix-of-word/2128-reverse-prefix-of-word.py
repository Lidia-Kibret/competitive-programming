class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        char = word.find(ch)
        if char == -1:
            return word
        chars = list(word)
        left , right = 0 , char
        while left < right:
            chars[left] , chars[right] = chars[right] , chars[left] 
            left += 1
            right -= 1
        return "".join(chars)        