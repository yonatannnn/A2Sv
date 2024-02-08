class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = {}
        ans = []
        s = 0
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] not in count:
                s += nums[i]
                count[nums[i]] = i
                i += 1
            else:
                ans.append(s)
                while nums[i] in count:
                    s -= nums[j]
                    count.pop(nums[j])
                    j += 1
        ans.append(s)
        return max(ans)
            