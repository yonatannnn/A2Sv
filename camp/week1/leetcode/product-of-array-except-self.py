class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = [0] * len(nums)
        list1[0] = 1
        list2 = [0] * len(nums)
        list2[-1] = 1
        product1 = 1
        product2 = 1

        for i in range(1,len(nums)):
            product1 *= nums[i-1]
            list1[i] = product1
        for i in range(len(nums)-2,-1,-1):
            product2 *= nums[i+1]
            list2[i] = product2
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = list1[i] * list2[i]
        return ans
        