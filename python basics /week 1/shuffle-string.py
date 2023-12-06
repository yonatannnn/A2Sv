class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        wordsDict = {}
        ind = 0
        ans = ""
        for index in indices:
            wordsDict[index] = s[ind]
            ind += 1 
        indices.sort()
        for i in indices:
            ans += wordsDict[i]
        return ans