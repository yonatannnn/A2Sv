class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        v = ["a" , "e" , "i" , "o" , "u"]
        vowels = {v[i]:0 for i in range(len(v))}
        count = 0
        maximum = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
                vowels[s[i]] += 1
        maximum = max(count , maximum)
        for j in range(k,len(s)):
            if s[j] in vowels:
                vowels[s[j]] += 1
                count += 1
            if s[j-k] in vowels:
                vowels[s[j-k]] -= 1
                count -=1
            maximum = max(count , maximum)
        return maximum
        
        