# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        length = defaultdict(list)
        def traverse(length , node , len):
            if node:
                length[len].append(node.val)
                traverse(length , node.left , len + 1)
                traverse(length , node.right , len + 1)
            return length
        ans = []
        length = traverse(length , root , 0)
        print(length)
        
        for depth in length:
            if depth % 2 == 1:
                length[depth].reverse()
        return length.values()



        