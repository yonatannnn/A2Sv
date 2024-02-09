from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = {0: -1}
        minimum_length = len(nums)
        running_sum = 0
        total = sum(nums)

        if total % p == 0:
            return 0

        if total < p:
            return -1

        for i in range(len(nums)):
            running_sum += nums[i]
            r = running_sum % p
            remain = (running_sum - total) % p
            if remain in remainder:
                minimum_length = min(minimum_length, i - remainder[remain])
            remainder[r] = i
        return minimum_length if minimum_length < len(nums) else -1
