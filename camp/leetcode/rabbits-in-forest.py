class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter(answers)
        ans = rabbits[0] if 0 in rabbits else 0
        for rabbit in answers:
            if rabbit == 0:
                continue
            else:
                if rabbits[rabbit] > 0:
                    ans += rabbit + 1
                    rabbits[rabbit] -= (rabbit + 1)
        return ans


        