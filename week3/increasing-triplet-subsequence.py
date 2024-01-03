class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minArray = [nums[0]]
        maxArray = [nums[-1]]
        f = len(nums) - 2
        for num in range(1,len(nums)):
            minArray.append(min(minArray[-1],nums[num]))
            maxArray.append(max(maxArray[-1],nums[f]))
            f -= 1
        maxArray.reverse()
        for num in range(len(nums)):
            if minArray[num] < nums[num] and maxArray[num] > nums[num]:
                return True
        return False
        