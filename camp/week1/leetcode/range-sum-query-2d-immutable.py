class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = []
        for i in self.matrix:
            prefixSum = [i[0]] * len(i)
            for j in range(1,len(i)):
                prefixSum[j] = prefixSum[j-1] + i[j]
            self.prefixSum.append(prefixSum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = 0
        for i in range(row1,row2+1):
            if col1 > 0:
                summ += (self.prefixSum[i][col2]-self.prefixSum[i][col1-1])
            else:
                summ += (self.prefixSum[i][col2])
        return summ
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)