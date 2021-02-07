# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        stack = []
        stack.append(root)
        unique_set = set()
        
        while stack:
            node = stack.pop()
            if k - node.val in unique_set:
                return True 
            unique_set.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False