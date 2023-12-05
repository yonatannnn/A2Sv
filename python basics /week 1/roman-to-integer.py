class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        numbers = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        current = float('inf')
        i = 0
        while i < len(s):
            if numbers[s[i]] <= current:
                num += numbers[s[i]]
            elif numbers[s[i]] > current:
                num += numbers[s[i]]-2 * current
            current = numbers[s[i]]
            i += 1
        return num

        