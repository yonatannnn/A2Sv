class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        f = collections.Counter(nums)
        ans = 0
        for i in range(len(nums)):
            new = {}
            for j in range(i , len(nums)):
                new[nums[j]] = 1
                if len(new) == len(f):
                    ans += 1
        return ans
        
        