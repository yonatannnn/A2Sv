class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 1
        count = 1
        answers = []
        while i < len(num):
            if num[i-1] == num[i]:
                count += 1
            else:
                count = 1
            if count == 3:
                answers.append(int(num[i]) * 111)
                count = 1
            i += 1
        if len(answers):
            big = max(answers)
            if big == 0:
                return "000"
            return str(big)
        else:
            return ""