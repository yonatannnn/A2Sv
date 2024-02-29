# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def find(values , node):
            if node:
                find(values , node.left)
                values.append(node.val)
                find(values , node.right)

            return values
        values = find([] , root)
        count = Counter(values)
        maximum = max(count.values())
        ans = []
        for key in count:
            if count[key] == maximum:
                ans.append(key)
        return ans
        
            
                

        