class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        value = 0
        signs = ["+","-","/","*"]
        for i in tokens:
            if i in signs:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                elif i == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack[0]