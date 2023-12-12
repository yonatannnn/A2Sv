class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(30):
            f = str(n)
            sum = 0
            for k in f:
                sum += (int(k)**2)
            if sum == 4:
                return False
            n = sum
        return True
        