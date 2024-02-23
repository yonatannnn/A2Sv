class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(n) < 10000000:
            if x == 0: return 0
            if n == 0: return 1
            r = x
            z = [1,2]
            while z[1] < abs(n):
                x = x * x
                z[0] = z[0] * 2
                z[1] = z[1] * 2
            i = abs(n) - z[0]
            for i in range(i):
                x = x * r
            if n >= 0:
                return x
            else: return 1/x
        def helper(x,n):
            if x == 0 : return 0
            if n == 0: return 1

            res = helper(x*x,n//2)
            return x * res if n % 2 else res
        res = helper(x,abs(n))
        return res if n >= 0 else 1/res