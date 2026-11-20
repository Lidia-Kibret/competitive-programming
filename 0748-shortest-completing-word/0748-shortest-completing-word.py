class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = {}

        for ch in licensePlate.lower():
            if ch.isalpha():
                count[ch] = count.get(ch, 0) + 1

        ans = ""

        for word in words:
            temp = {}

            for ch in word:
                temp[ch] = temp.get(ch, 0) + 1

            valid = True

            for ch in count:
                if temp.get(ch, 0) < count[ch]:
                    valid = False
                    break

            if valid:
                if ans == "" or len(word) < len(ans):
                    ans = word

        return ans