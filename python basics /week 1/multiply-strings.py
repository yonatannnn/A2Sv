class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = 0
        for i in range(len(num1)):
            number1 += int(num1[i]) * (10 ** (len(num1)-i-1))
        number2 = 0
        for i in range(len(num2)):
            number2 += int(num2[i]) * (10 ** (len(num2)-i-1))
        return f'{number1 * number2}'