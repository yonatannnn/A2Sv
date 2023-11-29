class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        z = []
        for i in strs:
            z.append(len(i))
        m = min(z)
        k = 0
        ans = ""
        for k in range(m):
            letter = strs[0][k]
            for f in range(len(z)):
                if strs[f][k] != letter:
                    return ans
            ans += letter
        return ans

        