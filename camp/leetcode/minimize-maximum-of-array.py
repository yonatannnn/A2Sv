class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            ans = max(ans , math.ceil(running_sum / (i + 1)))
        return ans
        