class Solution:
    def reverseWords(self, s: str) -> str:
        ch = s.split()
        reversed_ch = [c[::-1] for c in ch]
        return ' '.join(reversed_ch)

    
        