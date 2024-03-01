class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        j = 0
        length = len(senate)
        for i in senate:
            if i == "D":
                dire.append(j)
            else:
                radiant.append(j)
            j += 1
        while len(radiant) and len(dire):
            r = radiant.pop(0)
            d = dire.pop(0)
            if d > r:
                radiant.append(r + length)
            elif r > d:
                dire.append(d + length)
        return "Radiant" if len(radiant) else "Dire"
        