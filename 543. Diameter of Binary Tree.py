# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.result = 0
        
        def getHeight(node):
            
            if not node:
                return 0
            
            left = getHeight(node.left)
            right = getHeight(node.right)
            self.result = max(self.result, left+right)
            
            return max(left,right) + 1
        
        getHeight(root)
        return self.result
