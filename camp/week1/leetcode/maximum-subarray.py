class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        running_sum = float('-inf')
        for i in range(len(nums)):
            value = running_sum + nums[i]
            running_sum = max(nums[i] , value)
            maximum = max(maximum , running_sum)
        return maximum
