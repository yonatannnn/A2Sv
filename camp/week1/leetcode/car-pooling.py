class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ind = [0]  * 1001
        mi = float('inf')
        ma = float('-inf')
        for trip in trips:
            ma = max(ma , trip[2])
            mi = min(mi , trip[1])
            ind[trip[1]] += trip[0]
            ind[trip[2]] -= trip[0]
        ans = [ind[0]]
        if ans[0] > capacity:
            return False
        for i in range(1 , ma+1):
            value = ans[-1] + ind[i]
            if value > capacity:
                return False
            ans.append(value)
        return True        