# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find(stack , node , k):
            if node:
                find(stack , node.left , k)
                stack.append(node.val)
                find(stack , node.right , k)
            return stack
        return find([] , root , k)[k-1]

            
            

        