from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sMap = defaultdict(int)
        stMap = defaultdict(int)
        for i in range(len(s1)):
            sMap[s1[i]] += 1
            stMap[s2[i]] += 1
        if sMap == stMap:
            return True
        for i in range(len(s1) , len(s2)):
            stMap[s2[i]] += 1
            stMap[s2[i-len(s1)]] -= 1
            if stMap[s2[i-len(s1)]] == 0:
                stMap.pop(s2[i-len(s1)])
            if stMap == sMap:
                return True
        return False
        