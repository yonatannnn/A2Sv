class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        self.solve([], set(), set(), set(), n)
        return self.ans

    def solve(self, queens, xy_diff, xy_sum, row_set, n):
        row = len(queens)
        if row == n:
            self.ans += 1
            return

        for col in range(n):
            if col not in queens and row - col not in xy_diff and row + col not in xy_sum:
                queens.append(col)
                xy_diff.add(row - col)
                xy_sum.add(row + col)

                self.solve(queens, xy_diff, xy_sum, row_set, n)

                queens.pop()
                xy_diff.remove(row - col)
                xy_sum.remove(row + col)

    def create_board(self, queens):
        board = []
        n = len(queens)
        for row in range(n):
            row_str = ''.join(['Q' if col == queens[row] else '.' for col in range(n)])
            board.append(row_str)
        return board
