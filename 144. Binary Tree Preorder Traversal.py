# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Iteration 
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack = []
        stack.append(root)
        result = []
        
        if not root:
            return None 
        
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return result 

# Recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return [] 
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
