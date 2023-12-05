class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for i in candies:
            result.append((i + extraCandies) >=  maximum)
        return result        