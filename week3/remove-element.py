class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf')
            else:
                k += 1
        nums.sort()
        return k