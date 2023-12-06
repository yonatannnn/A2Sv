class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        lengths = []
        for ghost in ghosts:
            lengths.append(abs(ghost[0]-target[0]) + abs(ghost[1] - target[1]))
        minimum = min(lengths)
        if minimum <= abs(0-target[0]) + abs(0 - target[1]):
            return False
        return True
        