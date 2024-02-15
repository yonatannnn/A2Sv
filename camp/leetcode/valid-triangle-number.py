class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 1 , 1 , -1):
            right = i - 1
            value = nums[i]
            left = 0
            while left < right:
                if nums[left] + nums[right] > value:
                    ans += (right - left)
                    right -= 1
                else:
                    left += 1
        return ans

        