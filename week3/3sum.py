from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []     

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            target = 0 - nums[k]
            left, right = k + 1 , len(nums) - 1
            
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum == target:
                    result.append([nums[k], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
