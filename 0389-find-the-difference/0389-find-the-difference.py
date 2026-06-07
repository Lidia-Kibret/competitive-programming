class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for _ in t:
            if s.count(_) != t.count(_):
                return _
        