# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        max_sum = 0
        
        def traverse(node):
            nonlocal max_sum
            if not node: return 1, 0, None, None
            
            left_status, left_sum, left_min, left_max = traverse(node.left)
            right_status, right_sum, right_min, right_max = traverse(node.right)
            
            if ((left_status == 2 and left_max < node.val) or left_status == 1) and ((right_status == 2 and right_min > node.val) or right_status == 1):
                size = node.val + left_sum + right_sum
                max_sum = max(max_sum, size)
                return 2, size, (left_min if left_min is not None else node.val), (right_max if right_max is not None else node.val)
            return 0, None, None, None
        
        traverse(root)
        return max_sum
