# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not postorder or not inorder:
            return None 
        
        rootValue = postorder[-1]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        
        root.right = self.buildTree(inorder[inorderIndex+1:],postorder[inorderIndex:-1])
        root.left = self.buildTree(inorder[:inorderIndex],postorder[:inorderIndex])
        
        return root
