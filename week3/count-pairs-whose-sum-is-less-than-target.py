class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        right = len(nums) - 1
        ans = 0
        for left in range(len(nums)):
            if left >= right:
                break
            while left < right:
                if left >= right:
                    return ans
                if nums[left] + nums[right] < target:
                    break
                right -= 1
            pairs = right - left
            ans += pairs
        return ans

        