# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        if not pre:
            return None 
        
        root = TreeNode(post.pop())
        
        if len(pre) == 1:
            return root
        
        index = pre.index(post[-1])
        
        root.right = self.constructFromPrePost(pre[index:],post)
        root.left = self.constructFromPrePost(pre[1:index],post)        
        
        return root