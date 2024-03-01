class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False

        def find(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r ,c) in visited:
                return False
            visited.add((r , c))
            res = find(r + 1 , c , i + 1) or find(r - 1 , c , i + 1) or find(r , c + 1 , i + 1) or find(r , c - 1 , i + 1)
            visited.remove((r , c))
            return res

        for i in range(rows):
            for j in range(cols):
                if find(i , j , 0): return True
        return False
