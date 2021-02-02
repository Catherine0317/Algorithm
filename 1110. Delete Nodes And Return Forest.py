# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        result = []
        
        def delNodesRecu(node):
            if not node:
                return None 
            node.left = delNodesRecu(node.left)
            node.right = delNodesRecu(node.right)
            if node.val not in to_delete:
                return node 
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)
            return None 
        
        root = delNodesRecu(root)
        if root:
            result.append(root)
        return result 
