class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        store = {i:0 for i in range(len(nums)+1)}
        ZeroSum = 0
        OneSum = 0
        i = 1
        while i < len(nums) + 1:
            if nums[i-1] == 0:
                ZeroSum += 1
            store[i] = ZeroSum
            i += 1
        i = len(nums) - 1
        while i > -1:
            if nums[i] == 1:
                OneSum += 1
            store[i] = store[i] + OneSum
            i -= 1 
        maximum = max(store.values())
        ans = []
        for key in store:
            if store[key] == maximum:
                ans.append(key)
        return ans