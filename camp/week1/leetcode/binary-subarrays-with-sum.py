class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cumulative_sum_freq = {0: 1}
        current_sum = 0
        result_count = 0

        for num in nums:
            current_sum += num
            result_count += cumulative_sum_freq.get(current_sum - goal, 0)
            cumulative_sum_freq[current_sum] = cumulative_sum_freq.get(current_sum, 0) + 1

        return result_count
