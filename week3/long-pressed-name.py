class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        if name[i] != typed[j]:
            return False
        i += 1
        j += 1
        while j < len(typed) and i < len(name):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i-1] == typed[j]:
                j += 1
            else:
                return False
        for k in range(j,len(typed)):
            if name[i-1] != typed[k]:
                return False
        return True if i == len(name) else False
        