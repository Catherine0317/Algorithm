# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def helper(node):
            
            if not node:
                return 0
            
            left = helper(node.left)
            if left < 0:
                return -1
            
            right = helper(node.right)
            if right < 0:
                return -1 
            
            if abs(right-left) > 1:
                return -1
            
            return max(left,right) + 1
        
        return helper(root) >= 0
                
            
            
