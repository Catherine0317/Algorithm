# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def merge(t1, t2):
            
            if not t1 and not t2:
                return None 
            if not t1:
                return t2
            if not t2:
                return t1
            
            t1.left = merge(t1.left, t2.left)
            t1.right = merge(t1.right, t2.right)
        
            t1.val += t2.val
            return t1
        
        return merge(t1,t2)
        
            
            