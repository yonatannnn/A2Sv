class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for i in range(len(nums2)):
            value1 = nums2[i]
            if stack:
                while True:
                    value2 = stack.pop()
                    if value1 > value2:
                        res[value2] = value1
                    else:
                        stack.append(value2)
                        stack.append(value1)
                        break
                    if not stack:
                        stack.append(value1)
                        break

            else:
                stack.append(value1)
        while stack:
            last_element = stack.pop()
            res[last_element] = -1
        for i in range(len(nums1)):
            nums1[i] = res[nums1[i]]
        return nums1


            

        