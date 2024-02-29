from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        def backtrack(s , start , comb):
            if s == target:
                self.ans.append(comb.copy())
                return
            if start >= len(candidates) or sum(comb) > target:
                return
            for i in range(start , len(candidates)):
                if i > start and  candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                s += candidates[i]
                backtrack(s , i + 1 , comb)
                comb.pop()
                s -= candidates[i]
        backtrack(0 ,0 , [])
        return self.ans
