class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        Loses = {}
        for i in matches:
            Loses[i[0]] = 0 + Loses.get(i[0],0)
            Loses[i[1]] = 1 + Loses.get(i[1],0)
        noLose = []
        oneLose = []
        for j in Loses:
            if Loses[j] == 0:
                noLose.append(j)
            if Loses[j] == 1:
                oneLose.append(j)
        noLose.sort()
        oneLose.sort()
        return [noLose , oneLose]

        