class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        chance = True
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] > nums[j]:
                if not chance:
                    return False
                else:
                    chance = False
                if i > 0 and nums[i-1] > nums[j]:
                    nums[j] = nums[i]
            i += 1
            j += 1
        return True
