# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(arr: List[int] , node: TreeNode):
            if node:
                inOrder(arr , node.left)
                arr.append(node.val)
                inOrder(arr , node.right)
            return arr
        arr = inOrder([] , root)
        if len(set(arr)) < len(arr):
            return False
        return sorted(arr) == arr
        