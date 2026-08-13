class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        words = sentence.split()
        result = []

        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"

            new_word += "a" * i
            result.append(new_word)

        return " ".join(result)
        