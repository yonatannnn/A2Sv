class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remain = [1] + [0] * k
        summ = 0
        h = 0
        for i in nums:
            summ = (summ + i) % k
            h += remain[summ]
            remain[summ] += 1
        return h