class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill) - 1
        ans = skill[i] + skill[j]
        pairs = []
        while i < j:
            if ans != skill[i] + skill[j]:
                return -1
            pairs.append([skill[i],skill[j]])
            i += 1
            j -= 1
        answer = 0
        for i in pairs:
            answer += (i[0]*i[1])
        return answer


        