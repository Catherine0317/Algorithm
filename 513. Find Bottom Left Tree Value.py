from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        if not root:
            return None 
        
        queue = deque()
        queue.append(root)
       
        while queue:
            for i in range(len(queue)):
                root = queue.popleft()
                if i == 0:
                    result = root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return result 