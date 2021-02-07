# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        self.result = 0
        
        def sumleaves(node, is_left):
            if not node:
                return 0
            
            sumleaves(node.left, True)
            sumleaves(node.right, False)
            
            if not node.left and not node.right:
                if is_left:
                    self.result += node.val 
                else:
                    self.result += 0
                    
            return self.result 
                
        return sumleaves(root, False)