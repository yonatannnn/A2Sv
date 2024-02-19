class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        dicts = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in dicts:
                corresponding_element = check.pop() if check else "#"
                if dicts[char] != corresponding_element:
                    return False
            else:
                check.append(char)
        return not check