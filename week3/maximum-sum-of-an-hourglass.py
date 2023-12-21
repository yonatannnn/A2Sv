from collections import defaultdict
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum = 0
        for row in range(1,len(grid)-1):
            for col in range(1,len(grid[0])-1):
                s = grid[row][col] + grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1] + grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
                maximum = max(maximum,s)
        return maximum