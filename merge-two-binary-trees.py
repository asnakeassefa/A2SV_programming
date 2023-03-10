# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travers(self,root1,root2):
        if not root1 and not root2:
            return
        if root1 and root2:
            root1.val = root1.val + root2.val
            self.travers(root1.left,root2.left)
            self.travers(root1.right,root2.right)
        
        if root1 and root2 and not root1.left and root2.left:
            root1.left = root2.left
        if root1 and root2 and not root1.right and root2.right:
            root1.right = root2.right
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1:
            self.travers(root1,root2)
            return root1
        return root2