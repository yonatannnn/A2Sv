class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        limit = 0
        i = 0
        ans = 0
        length = len(nums)
        while limit < n:
            if i < length and nums[i] <= limit + 1:
                limit += nums[i]
                i += 1
            else:
                limit += (limit + 1)
                ans += 1
        return ans

        
        