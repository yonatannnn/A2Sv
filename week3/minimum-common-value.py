class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num1 = 0
        num2 = 0
        while num1 < len(nums1) and num2 < len(nums2):
            if nums1[num1] < nums2[num2]:
                num1 += 1
            elif nums1[num1] > nums2[num2]:
                num2 += 1
            else:
                return nums1[num1]
        return -1