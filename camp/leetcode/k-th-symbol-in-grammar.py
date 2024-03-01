class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        self.last = 2 ** (n-1)
        self.first = 0
        self.ans = 0
        def find(row):
            if row == n:
                return self.ans
            mid = (self.last + self.first) // 2
            if mid < k:
                self.first = mid
                self.ans = 1 if self.ans == 0 else 0
            else:
                self.last = mid + 1
                self.ans = 0 if self.ans == 0 else 1
            return find(row + 1)
        return find(1)
