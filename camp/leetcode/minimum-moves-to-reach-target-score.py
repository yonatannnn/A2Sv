class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        points = [0.5]
        ans = 0
        for i in range(maxDoubles , -1 , -1):
            value = 2 ** i
            add = target // value
            if add:
                points.append(add)
        for i in range(1 , len(points)):
            ans += (points[i] - points[i-1] * 2 + 1)
        return int(ans) - 1

        