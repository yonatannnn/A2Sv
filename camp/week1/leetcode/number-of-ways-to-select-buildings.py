class Solution:
    def numberOfWays(self, s: str) -> int:
        leftOne = [0]
        leftZero = [0]
        totalOne = 0
        for i in range(len(s)):
            if s[i] == '1':
                totalOne += 1
        totalZero = len(s) - totalOne
        rightZero = []
        rightOne = []
        for i in range(len(s)):
            if s[i] == '0':
                totalZero -= 1
                leftZero.append(leftZero[-1] + 1)
                leftOne.append(leftOne[-1])
            else:
                totalOne -= 1
                leftOne.append(leftOne[-1] + 1)
                leftZero.append(leftZero[-1])
            rightZero.append(totalZero)
            rightOne.append(totalOne)
        rightZero.append(0)
        rightOne.append(0)
        ans = 0
        for i in range(len(s)):
            if s[i] == '0':
                value = leftOne[i] * rightOne[i]
            else:
                value = leftZero[i] * rightZero[i]
            ans += value
        return ans