class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count = 0
        maximum = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                maximum = max(maximum,count)
                count = 0
            i += 1
        maximum = max(maximum,count)
        return maximum
        