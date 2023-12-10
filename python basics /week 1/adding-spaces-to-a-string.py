class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        i = 0
        j = 0
        while i < len(s):
            if j >= len(spaces):
                ans += s[i:]
                break
            if i == spaces[j]:
                ans += " "
                j += 1
            else:
                ans += s[i]
                i += 1
        return ans