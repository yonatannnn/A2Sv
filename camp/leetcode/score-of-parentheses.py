class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        output , val = 0 , 0
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                m = stack.pop()
                val = max(m * 2,1)
                if not stack:
                    output += val
                else:
                    stack[-1] += val
        return output
