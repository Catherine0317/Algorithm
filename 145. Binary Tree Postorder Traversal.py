# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Iteration
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack = []
        stack.append(root)
        result = []
        
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return result[::-1]

# Recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
