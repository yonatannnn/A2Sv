class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = [0] * (len(s)+1)
        for i in shifts:
            if i[2] == 0:
                letters[i[0]] -= 1
                letters[i[1]+1] += 1
            else:
                letters[i[0]] += 1
                letters[i[1]+1] -= 1
        prefix = [letters[0]] * len(letters)
        for i in range(1,len(letters)):
            prefix[i] = prefix[i-1] + letters[i]
        prefix.pop()
        ans = [0] * len(s)
        for i in range(len(prefix)):
            value = ord(s[i]) - ord("a") + prefix[i]
            real = value % 26
            r = ord("a") + real
            ans[i] = chr(r) 
        answer = "".join(ans)
        return answer




        
        