from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        ans = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                ans[row + col].append(mat[row][col])
        for key in ans:
            if key % 2 == 0:
                ans[key].reverse()
            answer.extend(ans[key])
        return answer
        

        
            
        