class Solution:
    def minimumSteps(self, s: str) -> int:
        zeroIndex = []
        for i in range(len(s)):
            if s[i] == '0':
                zeroIndex.append(i)
        ans = 0
        for i in range(len(zeroIndex)):
            value = zeroIndex[i] - i
            ans += value
        return ans
        