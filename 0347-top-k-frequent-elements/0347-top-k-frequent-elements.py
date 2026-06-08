class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_items = sorted(freq.items(), key= lambda x : x[1], reverse = True)
        return [num for num, count in sorted_items [:k]]
        