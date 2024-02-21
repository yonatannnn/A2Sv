class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = pow(5,(n + 1)//2,1000000007)
        odd = pow(4,n//2,1000000007)
        return even*odd % 1000000007

        