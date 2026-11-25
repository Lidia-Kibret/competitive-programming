class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        sa = sorted(range(n), key=lambda i: nums[i])

        rank = [0] * n

        for i in range(1, n):
            if nums[sa[i]] != nums[sa[i - 1]]:
                rank[sa[i]] = rank[sa[i - 1]] + 1
            else:
                rank[sa[i]] = rank[sa[i - 1]]

        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for i in range(1, n):
                a = sa[i - 1]
                b = sa[i]

                prev = (rank[a], rank[a + k] if a + k < n else -1)
                curr = (rank[b], rank[b + k] if b + k < n else -1)

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                continue

            j = sa[r - 1]

            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1

            lcp[r] = h

            if h > 0:
                h -= 1

        ans = n

        for r in range(n):
            left = lcp[r]
            right = lcp[r + 1] if r + 1 < n else 0

            length = max(left, right) + 1

            if length <= n - sa[r]:
                ans = min(ans, length)

        return ans