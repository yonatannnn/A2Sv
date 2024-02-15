class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        n = len(palindrome)
        if len(palindrome) <= 1:
            return ""
        for i in range(n // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return "".join(palindrome)
        palindrome[n - 1] = 'b'
        return "".join(palindrome)

                
            
        