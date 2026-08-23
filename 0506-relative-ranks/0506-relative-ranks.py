class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)

        rank = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                rank[s] = "Gold Medal"
            elif i == 1:
                rank[s] = "Silver Medal"
            elif i == 2:
                rank[s] = "Bronze Medal"
            else:
                rank[s] = str(i + 1)

        return [rank[s] for s in score]
        