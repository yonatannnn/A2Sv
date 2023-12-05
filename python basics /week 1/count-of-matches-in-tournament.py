import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        if n > 1 and n % 2 == 1:
            plus_one = True
        else:
            plus_one = False
        Bool = True
        while Bool:
           to_be = n // 2
           ans += to_be
           n = math.ceil(n/2)
           print(to_be)
           if to_be < 1:
               Bool = False
        return ans