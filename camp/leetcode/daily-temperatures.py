class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        k = 0
        for i in range(len(temperatures)):
            current = temperatures[i]
            if stack:
                while stack:
                    value = stack.pop()
                    if value[0] < current:
                        temperatures[value[1]] = i - value[1]
                        k += 1
                    else:
                        stack.append(value)
                        stack.append([current , i])
                        break
                    if not stack:
                        stack.append([current , i])
                        break
            else:
                stack.append([current , i])
        for i in range(len(stack)):
            temperatures[stack[i][1]] = 0
        return temperatures
