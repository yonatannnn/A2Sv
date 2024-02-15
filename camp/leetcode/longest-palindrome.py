class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        maximum = 0
        ans = 0
        odd_found = False
        for key in count:
            if count[key] % 2 == 0:
                ans += count[key]
            else:
                ans += count[key] - 1
                odd_found = True
        return ans if not odd_found else ans + 1
        