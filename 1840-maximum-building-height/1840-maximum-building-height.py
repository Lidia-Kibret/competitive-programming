class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions += [[1, 0], [n, n - 1]]
        restrictions.sort()
        
        for i in range(1, len(restrictions)):
            d = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i - 1][1] + d)
        for i in range(len(restrictions) - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1],
                                     restrictions[i + 1][1] + d)
        

        ans = 0
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]
            ans = max(ans, (h1 + h2 + x2 - x1) // 2)

        return ans