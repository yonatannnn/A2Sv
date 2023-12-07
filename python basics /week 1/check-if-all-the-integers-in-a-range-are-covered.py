class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        r = set()
        for i in ranges:
            for j in range(i[0],i[1]+1):
                r.add(j)
        for i in range(left,right+1):
            if i not in r:
                return False
        return True
