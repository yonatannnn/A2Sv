class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def min_max(sum_, l, r, f_turn=True):
            if l == r:
                if f_turn:
                    return sum_ + nums[l]
                else:
                    return sum_ - nums[l]
            if f_turn:
                return max(min_max(sum_ + nums[l], l+1, r, False),
                           min_max(sum_ + nums[r], l, r - 1, False))
            else:
                return min(min_max(sum_ - nums[l], l+1, r, True),
                           min_max(sum_ - nums[r], l, r - 1, True))
        
        res = min_max(0, 0, len(nums) - 1)
        return res >= 0