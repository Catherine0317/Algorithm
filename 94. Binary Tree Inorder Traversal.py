# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Iteration
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack = []
        result = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

# Recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
