class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        length = []
        for i in words:
            length.append(len(i))
        maximum = max(length)
        minimum = min(length)
        mainAns = []
        for j in range(maximum):
            ans = ""
            for word in words:
                try:
                    ans += word[j]
                except:
                    ans += " "
            ans = ans.rstrip()
            mainAns.append(ans)
        return mainAns