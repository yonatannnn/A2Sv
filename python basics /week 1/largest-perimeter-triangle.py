class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 1
        j = len(nums) - 2
        k = len(nums) - 3
        while k > -1:
            if nums[k] + nums[j] > nums[i]:
                return nums[k] + nums[j] + nums[i]
            k -= 1
            i -= 1
            j -= 1
        return 0
        