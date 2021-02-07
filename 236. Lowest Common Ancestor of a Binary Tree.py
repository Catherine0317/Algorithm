# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def CommonAncestor(node, p, q):
            
            if not node:
                return None 
            elif node == p or node == q:
                return node
            
            left = CommonAncestor(node.left, p, q)
            right = CommonAncestor(node.right, p, q)
            
            if left and right:
                return node 
            return left or right 
        
        return CommonAncestor(root, p, q)
                