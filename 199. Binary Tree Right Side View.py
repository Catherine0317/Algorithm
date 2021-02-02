from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            return None 
        
        result = []
        queue = deque()
        queue.append(root)
        
        while len(queue) != 0:
            curr_level = []
            for _ in range(len(queue)):
                root = queue.popleft()
                curr_level.append(root.val)
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
            result.append(curr_level[0])
        return result 
                
