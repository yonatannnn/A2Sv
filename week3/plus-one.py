class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Answer = []
        num = ""
        for i in digits:
            num = num + str(i)
        intnum = int(num)
        plusOneDigit = intnum + 1
        newDigit = str(plusOneDigit)
        for i in newDigit:
            Answer.append(int(i))
        return Answer