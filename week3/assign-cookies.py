class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        ans = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                ans += 1
                child += 1
                cookie += 1
            else:
                cookie += 1
        return ans