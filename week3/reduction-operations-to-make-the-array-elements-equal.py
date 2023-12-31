class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[0]
        unique = 0
        counter = {}
        before_number = {}
        ans = 0
        for i in nums:
            counter[i] = 1 + counter.get(i,0)
            if i not in before_number:
                before_number[i] = unique
                unique += 1
        for i in counter:
            Each_step = counter[i] * before_number[i]
            ans += Each_step
        return ans