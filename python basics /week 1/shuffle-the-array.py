class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        myList = []
        i =0
        n2 = n
        while i< n2:
            myList.append(nums[i])
            myList.append(nums[n])
            i = i + 1
            n = n + 1
        return myList