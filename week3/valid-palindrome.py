class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphas = []
        for i in s:
            if i.isalpha() or i.isnumeric():
                alphas.append(i)
        print(alphas)
        k = 0
        print(reversed(alphas))
        for i in reversed(alphas):
            if i != alphas[k]:
                return False
            k += 1
        return  True
        