class Solution:
    def decodeString(self, s: str) -> str:
        brackets = []
        string = []
        current = ''
        numbers = []
        currDigit = ''
        for i in range(len(s)):    
            if s[i] == '[':
                numbers.append(int(currDigit))
                currDigit = ''
                string.append(current)
                brackets.append('[')
                current = ''
            elif s[i] == ']':
                brackets.pop()
                num = numbers.pop()
                new_str = current * num
                if brackets:
                    last_str = string.pop()
                    current = last_str + new_str
                else:
                    string.append(new_str)
                    current = ''
            elif s[i].isdigit():
                currDigit += s[i]
            else:
                current += s[i]
        if current:
            string.append(current)
        ans = ''
        for i in string:
            if i:
                ans += i
        return ans
                    


        
        