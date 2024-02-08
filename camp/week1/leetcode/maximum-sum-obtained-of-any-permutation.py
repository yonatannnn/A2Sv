class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        p = [0] * len(nums)
        for i in requests:
            p[i[0]] += 1
            if i[1] < len(nums)-1:
                p[i[1]+1] -= 1
        prefixSum = [p[0]] * len(p)
        for i in range(1,len(p)):
            prefixSum[i] = prefixSum[i-1] + p[i]
        prefixSum.sort(reverse = True)
        nums.sort()
        ans = 0
        for i in prefixSum:
            ans += i * nums.pop()
        return ans %(10**9 + 7)