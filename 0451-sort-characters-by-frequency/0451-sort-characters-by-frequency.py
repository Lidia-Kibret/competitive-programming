class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_char = sorted(freq.items(), key=lambda x : x[1], reverse = True)
        result = ""
        for key, value in sorted_char:
            result += key * value
        return result 
        

        