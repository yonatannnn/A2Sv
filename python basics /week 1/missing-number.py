class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Dict = {}
        for index , value in enumerate(nums):
            Dict[value] = index
        for i in range(len(nums)+1):
            if i not in Dict:
                return i