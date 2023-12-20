class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            ans.append([0 for i in range(len(matrix))]) 
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                ans[column][row] = matrix[row][column]
        return ans
        