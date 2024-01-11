class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dict = { "B" : 0 , "W" :0 }
        ans = 0
        for i in range(k):
            dict[blocks[i]] += 1
        ans = dict["W"]
        for j in range(k,len(blocks)):
            dict[blocks[j]] += 1
            dict[blocks[j-k]] -= 1
            ans = min(ans , dict["W"])
        return ans 