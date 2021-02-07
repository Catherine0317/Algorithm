# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def findmin(node):
            
            while node.left:
                node = node.left 
            return node
        
        if not root:
            return None 
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None 
            elif not root.left:
                root = root.right 
            elif not root.right:
                root = root.left 
            else:
                p = findmin(root.right)
                root.val = p.val 
                root.right = self.deleteNode(root.right, p.val)
        return root 
        
        
            