class Solution:
    def minSteps(self, s: str, t: str) -> int:
         count_s = {}
         for char in s:
            count_s[char] = count_s.get(char, 0) + 1
         count_t = {}
         for char in t:
            count_t[char] = count_t.get(char, 0) + 1
         steps = 0
         for char in count_t:
            diff = count_t[char] - count_s.get(char, 0)
            if diff > 0:
                steps += diff
         return steps
        