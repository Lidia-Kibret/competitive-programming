class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_sum = sum(skill)
        if total_sum % (n // 2) != 0:
            return -1
    
        target = total_sum // (n // 2)
        skill.sort()

        i, j = 0, n - 1
        chemistry = 0
        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            chemistry += skill[i] * skill[j]
            i += 1
            j -= 1

        return chemistry
        