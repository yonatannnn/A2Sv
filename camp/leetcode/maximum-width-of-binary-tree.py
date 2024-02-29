from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.level = defaultdict(list)

        def find(y, x, node):
            if node:
                self.level[y].append((x, node.val))
                find(y + 1, x * 2, node.left)
                find(y + 1, x * 2 + 1, node.right)

        find(0, 0, root)
        ans = 0

        for level in self.level.values():
            level.sort()
            width = level[-1][0] - level[0][0] + 1
            ans = max(ans, width)

        return ans
