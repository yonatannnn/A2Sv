# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 
        def findMin(minimum , maximum , node):
            if node:
                minimum = min(minimum , node.val)
                maximum = max(maximum , node.val)
                self.ans = max(self.ans , maximum - minimum)
                findMin(minimum , maximum , node.left)
                findMin(minimum , maximum , node.right)
        findMin(root.val , root.val , root)
        return self.ans