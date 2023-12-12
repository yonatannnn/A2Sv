class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i].strip()
        j = len(words) - 1
        ans = []
        while j > -1:
            if (len(words[j])):
                ans.append(words[j])
            j -= 1
        return " ".join(ans)
        