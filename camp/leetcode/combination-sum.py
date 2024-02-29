class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        def backtrack(comb):
            if sum(comb) == target:
                sor = sorted(comb)
                self.ans.add(tuple(sor))
            if sum(comb) > target:
                return
            for i in range(len(candidates)):
                comb.append(candidates[i])
                backtrack(comb)
                comb.pop()
        backtrack([])
        return list(self.ans)
        