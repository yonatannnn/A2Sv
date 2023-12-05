class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        myList = []
        for i in range(len(nums)):
            myList.append(nums[i])
        for i in range(len(nums)):
            myList.append(nums[i])
        return myList