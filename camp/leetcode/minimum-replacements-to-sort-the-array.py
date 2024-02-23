class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        splits = 0
        
        for current_idx in reversed(range(1, N)):
            previous, current = nums[current_idx - 1], nums[current_idx]
            
            if previous > current:
                quotient = previous // current
                remainder = previous % current
                
                if remainder == 0:
                    nums[current_idx - 1] = current
                    splits += quotient - 1
                else:
                    nums[current_idx - 1] = previous // (quotient + 1)
                    splits += quotient
        
        return splits
