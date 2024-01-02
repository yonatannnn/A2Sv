class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        non_zero = 0
        while non_zero < len(nums):
            if nums[non_zero] != 0:
                nums[zero] , nums[non_zero] = nums[non_zero] , nums[zero]
                zero += 1
            non_zero += 1
        return nums 
        
        