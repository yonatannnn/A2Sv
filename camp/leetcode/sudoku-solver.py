class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    box_id = (i // 3) * 3 + j // 3
                    boxes[box_id].add(int(board[i][j]))

        def backtrack(i , j):
            nonlocal solved
            if i == 9:
                solved = True
                return

            new_i = i + (j+1) // 9
            new_j = (j+1) % 9
            if board[i][j] != '.':
                backtrack( new_i,new_j )
            else:
                for candidate in range(1 , 10):
                    box_id = (i // 3) * 3 + j // 3
                    if candidate not in rows[i] and candidate not in cols[j] and candidate not in boxes[box_id]:
                        rows[i].add(candidate)
                        cols[j].add(candidate)
                        boxes[box_id].add(candidate)
                        board[i][j] = str(candidate)

                        backtrack(new_i , new_j)

                        if not solved:
                            rows[i].remove(candidate)
                            cols[j].remove(candidate)
                            boxes[box_id].remove(candidate)
                            board[i][j] = '.'
        solved = False
        backtrack(0 , 0)





        