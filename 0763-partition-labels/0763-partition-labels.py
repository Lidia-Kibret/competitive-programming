class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        result = []
        start = 0
        end = 0

        for i in range(len(s)):
            end = max(end , last[s[i]])
            if i == end:
                size = end - start + 1
                result.append(size)
                start = i + 1
        return result 
        

        