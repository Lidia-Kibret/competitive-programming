class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        sort_items = sorted(result.items(), key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sort_items[i][0])
        return res

        
        