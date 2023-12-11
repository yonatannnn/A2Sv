from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        countDict = Counter(arr)
        minimum = 0.25 * length
        for i in countDict:
            if countDict[i] > minimum:
                return i
        