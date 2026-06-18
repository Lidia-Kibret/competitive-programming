class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        letter={ch:i for i,ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
        ans = ""

        for word in words:
            total=0
            for ch in word:
                total+=weights[letter[ch]]
            total%=26
            total=25-total

            ans+=chr(97+total)
        return ans

       