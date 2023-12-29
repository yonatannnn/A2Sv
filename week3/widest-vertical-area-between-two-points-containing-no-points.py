class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maximum = 0
        for point in range(1,len(points)):
            dif = points[point][0] - points[point-1][0]
            maximum = max(dif,maximum)
        return maximum

        