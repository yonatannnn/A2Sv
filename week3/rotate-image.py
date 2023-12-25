class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(row + 1 , len(matrix[0])):
                matrix[col][row] , matrix[row][col] = matrix[row][col] , matrix[col][row]
        for row in matrix:
            row.reverse()
        # transpose = []
        # for i in range(len(matrix)):
        #     transpose.append([0 for j in range(len(matrix))])
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         transpose[col][row] = matrix[row][col]
        # for row in transpose:
        #     row.reverse()
        # for row in range(len(transpose)):
        #     for col in range(len(transpose)):
        #         matrix[row][col] = transpose[row][col]
        
