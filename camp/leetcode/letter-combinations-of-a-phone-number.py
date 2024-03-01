class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.ans = []
        def backtrack(ind , temp):
            if ind == len(digits):
                string = "".join(temp)
                self.ans.append(string)
                return
                
            currInx = digits[ind]
            for i in range(len(letters[currInx])):
                backtrack(ind + 1 , temp + letters[currInx][i])

        backtrack(0 , '')
        return self.ans