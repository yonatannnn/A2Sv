class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = {}
        stack = []
        twice = len(nums) * 2
        for j in range(twice):
            i = j % len(nums)
            if stack:
                while True:
                    index = stack.pop()
                    if nums[index] < nums[i]:
                        res[index] = nums[i]
                    else:
                        stack.append(index)
                        stack.append(i)
                        break
                    if not stack:
                        stack.append(i)
                        break
            else:
                stack.append(i)
        for i in range(len(nums)):
            nums[i] = res.get(i , -1)
        return nums