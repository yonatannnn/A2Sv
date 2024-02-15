class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bracket = {
            'open' : 0,
            'close' : 0
        }
        count = 0
        for i in range(len(s)):
            if s[i] == ')':
                if bracket['open']:
                    bracket['open'] -= 1
                else:
                    count += 1
            else:
                bracket['open'] += 1
        return count + bracket['open']

        