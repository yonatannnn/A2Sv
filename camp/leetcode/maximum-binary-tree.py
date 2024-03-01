# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums):
            if not nums:
                return None
            m = max(nums)
            idx = nums.index(m)
            new_node = TreeNode(m)
            new_node.left = build(nums[:idx])
            new_node.right = build(nums[idx+1 : ])
            return new_node

        return build(nums)