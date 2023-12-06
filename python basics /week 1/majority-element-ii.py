class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = len(nums)/3
        outPut = []
        for i in nums:
            if nums.count(i) > a and i not in outPut:
                outPut.append(i)
        return outPut
        