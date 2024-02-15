class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        end = points[0][1]
        count = 0
        for i in range(len(points)):
            if points[i][0] <= end:
                pass
            else:
                end = points[i][1]
                count += 1
        count += 1
        return count
        
        