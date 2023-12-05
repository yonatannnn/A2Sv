class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = ""
        maximum = max(len(word1),len(word2))
        while i < maximum:
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
            i += 1
        return ans