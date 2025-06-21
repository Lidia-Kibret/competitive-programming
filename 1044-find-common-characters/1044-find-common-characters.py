class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for word in words[1:]:
            count &= Counter(word)
        return list(count.elements())