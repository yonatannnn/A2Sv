class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(mat):
            for i in mat:
                for j in i:
                    if i.count(j) > 1 and j != ".":
                        return False
            return True

        def check3(mat,row,col):
            l = []
            for i in range(row,row+3):
                for j in range(col,col+3):
                    print(mat[i][j])
                    if mat[i][j] == ".":
                        continue
                    elif mat[i][j] not in l:
                        l.append(mat[i][j])
                    else:
                        return False
            return True
        if not check(board):            
            return False
        print("x")
        n = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        if not check(n):
            return False
        row = 0
        col = 0
        for i in range(row,9,3):
            for j in range(col,9,3):
                if not check3(board,i,j):
                    return False
        return True

        