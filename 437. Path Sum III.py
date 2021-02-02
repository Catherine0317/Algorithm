# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n^2)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        if not root:
            return 0
        
        def dfs(node, target):
            
            count = 0
            
            if not node:
                return 0
            
            if target - node.val == 0:
                count += 1
                
            count += dfs(node.left, target - node.val)
            count += dfs(node.right,target - node.val)
            return count
        
        return dfs(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right, sum)
    
# O(n)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        self.result = 0
        dic = {0:1}
        
        def dfs(root, sum, cur, dic):
            if not root:
                return None
            
            cur += root.val 
            pre = cur - sum 
            
            self.result += dic.get(pre,0)
            dic[cur] = dic.get(cur,0) + 1
            dfs(root.left, sum, cur, dic)
            dfs(root.right, sum, cur, dic)
            dic[cur] -= 1
        
        dfs(root,sum,0,dic)
        return self.result 
