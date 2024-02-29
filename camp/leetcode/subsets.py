class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        def backtrack(start , comb):
            self.ans.add(tuple(comb.copy()))
            for i in range(start , len(nums)):
                comb.append(nums[i])
                backtrack(i + 1 , comb)
                comb.pop()
        backtrack(0 , [])
        return list(self.ans)
        