# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root):
        if root and not root.right and not root.left:
            return str(root.val)
        left = None
        right = None
        if root and root.left:
            left = self.DFS(root.left)
        if root and root.right:
            right = self.DFS(root.right)
        if left and right:
            return str(root.val) + "(" + left + ")" + "(" + right + ")"
        elif left:
            return str(root.val) + "(" + left + ")"
        elif right:
            return str(root.val) + "()"+"(" + right + ")"
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = self.DFS(root)
        return ans