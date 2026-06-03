class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for num in arr:
            r = num % k
            freq[r] += 1

        if freq[0] % 2 != 0:
            return False

        for r in range(1, k // 2 + 1):
            if freq[r] != freq[k -r]:
                return False
        return True


        
        