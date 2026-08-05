class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(len(points)):
            dist = defaultdict(int)

            for j in range(len(points)):
                if i == j:
                    continue

                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                d = dx * dx + dy * dy

                dist[d] += 1

            for count in dist.values():
                ans += count * (count - 1)

        return ans
        