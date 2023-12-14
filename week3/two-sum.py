class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i in range(len(nums)):
            
            n = target - nums[i]
            if n in dicts:

                return [nums.index(n),i]
            else :
                dicts[nums[i]] = n


    
