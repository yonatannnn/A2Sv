class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        for i in range(k):
            summ += nums[i]
        j = k
        ans = summ/k
        while j < len(nums):
            summ += nums[j]
            summ -= nums[j-k]
            ans = max(ans , summ/k)
            j += 1
        return ans 

        