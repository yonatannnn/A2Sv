class Solution:
    def freqAlphabets(self, s: str) -> str:
        map = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
        j = len(s) - 1
        ans = ""
        while j > -1:
            if s[j] == "#":
                ans = map[int(s[j-2:j])] + ans
                j -= 3
            else:
                ans = map[int(s[j])] + ans
                j -= 1
        return ans
        