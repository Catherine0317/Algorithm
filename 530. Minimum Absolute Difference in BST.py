# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
    
        self.prev = None
        self.difference = float('inf')
        
        def inorder(node):
            
            if not node:
                return None
            
            inorder(node.left)
            if self.prev:
                self.difference = min(self.difference, abs(node.val - self.prev.val))
            self.prev = node
            inorder(node.right)
            return self.difference
            
        return inorder(root)
            
                
        