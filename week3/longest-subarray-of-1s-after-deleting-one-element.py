class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones = 0
        zeros = 0
        current = 0
        max_lens = []

        if nums.count(0) == 0:
            return len(nums) - 1

        for num in nums:
            if num == 1:
                if zeros != 0:
                    ones += 1
                    current += 1
                else:
                    ones += 1
            else:
                zeros += 1
                if zeros % 2 == 0:
                    max_lens.append(ones)
                    ones = 0
                else:
                    max_lens.append(current)
                    current = 0

        max_lens.append(ones)
        max_lens.append(current)

        return max(max_lens)
