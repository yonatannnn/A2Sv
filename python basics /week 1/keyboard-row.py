class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        def checkRow(letter):
            row1 = "qwertyuiop"
            row2 = "asdfghjkl"
            row3 = "zxcvbnm"
            if letter in row1:
                return 1
            if letter in row2:
                return 2
            if letter in row3:
                return 3
        for word in words:
            for i in range(len(word)-1):
                if checkRow(word[i].lower()) != checkRow(word[i+1].lower()):
                    break
            else:
                ans.append(word)
        return ans