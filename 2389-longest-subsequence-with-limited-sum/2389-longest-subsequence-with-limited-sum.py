class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix = []
        total = 0

        for num in nums:
            total += num
            prefix.append(total)

        answer = []

        for query in queries:
            count = 0

            for total in prefix:
                if total <= query:
                    count += 1
                else:
                    break

            answer.append(count)

        return answer