class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        piles.sort()
        n = len(piles)
        j = 0
        for i in range(n-2,-1,-2):
            count += piles[i]
            j += 1
            if j >= i:
                break
        return count
        
        