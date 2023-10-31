# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(root,left):
            if root and not root.left and not root.right:
                if left:
                    ans[0] += root.val
            
            if root.left:
                dfs(root.left,True)
            if root.right:
                dfs(root.right,False)
        dfs(root,False)
        return ans[0]