class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = 0
        col = len(mat) - 1
        s = 0
        while row < len(mat):
            s += mat[row][row]
            s += mat[row][col]
            row += 1
            col -= 1
        if len(mat) % 2 == 1:
            s -= (mat[len(mat)//2][len(mat)//2])
        return s
