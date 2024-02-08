class Solution:
    def maxScore(self, s: str) -> int:
        zero = []
        z = 0
        o = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                z += 1
            zero.append(z)
        s = s[::-1]
        one = []
        for i in range(1 , len(s)):
            if s[i-1] == '1':
                o += 1
            one.append(o)
        one.reverse()
        ans = 0
        for i in range(len(one)):
            value = one[i] + zero[i]
            ans = max(value , ans)
        return ans


