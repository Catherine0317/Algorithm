# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        self.total = 0
        
        def convert(node):
            
            if not node:
                return None
            
            node.right = convert(node.right)
            self.total += node.val
            node.val = self.total
            node.left = convert(node.left)
            return node 
        
        return convert(root)