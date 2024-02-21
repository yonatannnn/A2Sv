class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        def swap(s , i , j):
            if i >= j:
                return
            s[i] , s[j] = s[j] , s[i]
            return swap(s , i + 1 , j - 1)

        swap(s , i , j)
            
        """
        Do not return anything, modify s in-place instead.
        """
        