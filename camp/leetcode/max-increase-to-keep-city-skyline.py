class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        count = 0
        maxRow = []
        maxCol = []
        row = len(grid)
        column = len(grid[0])
        for i in grid:
            maxRow.append(max(i))
        rez = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        for i in rez:
            maxCol.append(max(i))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                m = min(maxRow[i],maxCol[j])
                if  m > grid[i][j]:
                    count = count + m - grid[i][j]
        return count 

        