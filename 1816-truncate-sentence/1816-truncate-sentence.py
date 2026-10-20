class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        result = words[:k]
        return " ".join(result)
        