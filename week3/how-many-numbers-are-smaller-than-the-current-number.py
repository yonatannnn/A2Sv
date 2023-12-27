class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newArr = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                a = nums[i]
                if a > nums[j]:
                    count += 1
            newArr.append(count) 
        return newArr