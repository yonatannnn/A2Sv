# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minimum = min(p.val , q.val)
        maximum = max(p.val , q.val)
        def find(minimum , maximum , node):
            if node:
                if minimum < node.val and maximum > node.val or minimum == node.val or maximum == node.val:
                    return node
                elif minimum > node.val:
                    return find(minimum , maximum , node.right)
                else:
                    return find(minimum , maximum , node.left)
        return find(minimum , maximum , root)
        
        