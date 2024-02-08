class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        j = 0
        ans = []
        while j < len(s):
            count[s[j]] = 1 + count.get(s[j],0)
            if sum(count.values()) - max(count.values()) <= k:
                ans.append(sum(count.values()))
            else:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    count.pop(s[i])
                i += 1
            j += 1
        return max(ans)

        