class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i = 0
        j = 0
        count = 0 
        less = []
        greater = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                greater.append(nums[i])
            elif nums[i] < pivot:
                less.append(nums[i])
            else:
                count += 1
        ans = less + [pivot] * count + greater
        return ans