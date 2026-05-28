class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in range(len(strs)):
            word = strs[i]
            ch = sorted(word)

            key = "".join(ch)

            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]
        return list(result.values())
    
        