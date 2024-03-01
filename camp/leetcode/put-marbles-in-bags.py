class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = []
        for i in range(len(weights) - 1):
            pairs.append(weights[i] + weights[i+1])
        pairs.sort()
        pre = []
        rs = 0
        for i in range(len(pairs)):
            rs += pairs[i]
            pre.append(rs)
        maximum = 0
        minimum = 0
        for i in range(k-1):
            maximum += pairs[-1 - i ]
            minimum += pairs[i]
        return maximum - minimum
        