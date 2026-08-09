class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")

        paragraph = paragraph.split()

        count = {}

        for word in paragraph:
            if word not in banned:
                count[word] = count.get(word, 0) + 1

        answer = max(count, key=count.get)

        return answer