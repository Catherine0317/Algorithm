# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def isSame(t1,t2):
            
            if not t1 and not t2:
                return True 
            if not t1 or not t2:
                return False 
            
            return t1.val == t2.val and isSame(t1.left, t2.left) and isSame(t1.right,t2.right)
            
        if not s and not t:
            return True 
        if not s or not t:
            return False 
        return isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)