class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        possible = []
        z = k
        s = 0
        sums = []
        for _ in range(k):
            possible.append(cardPoints[z*-1])
            z -= 1
        for i in range(k):
            possible.append(cardPoints[i])
        for i in range(k):
            s += possible[i]
        sums = s
        for i in range(k , len(possible)):
            s += possible[i]
            s -= possible[i-k]
            sums = max(s , sums)
        return sums