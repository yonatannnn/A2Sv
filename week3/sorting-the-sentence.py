class Solution:
    def sortSentence(self, s: str) -> str:
        newList = s.split(" ")
        newList.sort(key = lambda x:int(x[-1]))
        result = ""
        for word in newList:
            result = result +  word[:-1] + " "
        
        return result.strip()