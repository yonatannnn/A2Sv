class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        i = 0
        j = 0
        ans = [1]
        visited = []        
        while j < len(s):
            if s[j] in visited:
                ans.append(len(visited))
                i = s.index(s[j],i) + 1
                visited = []
                j = i
            else:
                visited.append(s[j])
                j += 1
        ans.append(len(visited))
        return max(ans)