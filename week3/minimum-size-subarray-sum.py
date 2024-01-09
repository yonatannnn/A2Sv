class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        ans = []
        i = 0
        j = 0
        while  i < len(nums):
            if summ >= target:
                ans.append(i - j)
                summ -= nums[j]
                j += 1
            else:
                summ += nums[i]
                i += 1

        while summ >= target and j < i:
            if summ >= target:
                ans.append(i - j)
                summ -= nums[j]
            else:
                summ -= nums[j]
            j += 1
        return min(ans) if len(ans) > 0 else 0