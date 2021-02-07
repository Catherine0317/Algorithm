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
        
            if node.val > p.val and node.val > q.val:
                return CommonAncestor(node.left, p, q)
            elif node.val < p.val and node.val < q.val:
                return CommonAncestor(node.right, p, q)
            else:
                return node 
            
        return CommonAncestor(root, p, q)