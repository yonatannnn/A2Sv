class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numChange = {}
        changedNum = {}
        i = 0
        for i in operations:
            if i[0] in changedNum:
                numChange[changedNum[i[0]]] = i[1]
                changedNum[i[1]] = changedNum[i[0]]
                changedNum.pop(i[0])
            else:
                numChange[i[0]] = i[1]
                changedNum[i[1]] = i[0]
        for i in range(len(nums)):
            if nums[i] in numChange:
                nums[i] = numChange[nums[i]]
        return nums