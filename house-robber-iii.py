# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dp(self,root,memo):
        if not root:
            return 0
        temp = 0
        if root in memo:
            return memo[root]
        if root.left:
            temp += self.dp(root.left.left,memo) + self.dp(root.left.right, memo)
        if root.right:
            temp += self.dp(root.right.left,memo) + self.dp(root.right.right,memo)
        
        memo[root] = max(self.dp(root.left,memo)+self.dp(root.right,memo),temp+root.val)
        return memo[root]
    def rob(self, root: Optional[TreeNode]) -> int:

        return self.dp(root,{})