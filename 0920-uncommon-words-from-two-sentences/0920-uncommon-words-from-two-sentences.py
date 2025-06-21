class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
         count = Counter(s1.split() + s2.split())
         return [word for word, freq in count.items() if freq == 1]
        