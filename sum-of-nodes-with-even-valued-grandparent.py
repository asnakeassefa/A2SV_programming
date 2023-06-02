# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,gp,p,ans):
        if not root:
            return
        
        if gp % 2 == 0:
            ans[0] += root.val
        self.dfs(root.left,p,root.val,ans)
        self.dfs(root.right,p,root.val,ans)
            
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = [0]
        self.dfs(root,-1,-1,ans)
        return ans[0]