class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = 0
        for i in range(r,len(nums)):
            if nums[i] == 0:
                nums[r],nums[i] = nums[i] ,nums[r]
                r += 1
        for i in range(r,len(nums)):
            if nums[i] == 1:
                nums[r],nums[i] = nums[i] ,nums[r]
                r += 1