class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jump = 0
        i = 0
        while i < len(nums):
            if can_jump < 0:
                return False
            elif nums[i] > can_jump:
                can_jump = nums[i]
            can_jump -= 1
            i += 1
        return True


        