class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        k = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                k += 1
                i = j
            else:
                nums[j] = float('inf')
            j += 1
        nums.sort()
        return k
        