# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrderTraversal(self, root):
        if not root:
            return 
        self.inOrderTraversal(root.left)
        self.inOrderList.append(root)
        self.inOrderTraversal(root.right)
        return 
    
    def createBalancedBST(self, low, high):
        if low > high:
            return None

        mid = low + high >> 1
        
        node = self.inOrderList[mid]
        node.left = self.createBalancedBST(low, mid - 1)
        node.right = self.createBalancedBST(mid + 1, high)
        
        return node
        
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inOrderList = []
        self.inOrderTraversal(root)
        return self.createBalancedBST(0, len(self.inOrderList)-1)
