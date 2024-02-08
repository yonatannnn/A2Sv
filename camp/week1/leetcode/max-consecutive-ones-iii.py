class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        dict = {1:0 , 0:0}
        left = 0
        right = 0
        maximum = 0
        while right < len(nums):
            while dict[0] > k:
                dict[nums[left]] -= 1
                left += 1
            maximum = max(maximum , sum(dict.values()))
            dict[nums[right]] += 1
            right += 1
        if dict[0] <= k:
            maximum = max(maximum , sum(dict.values()))
        return maximum


                
        