# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self,root1,root2):
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif root1 and not root2:
            return False
        elif root1.val != root2.val:
            return False
        
        left = self.checkSymmetry(root1.right,root2.left)
        right = self.checkSymmetry(root1.left,root2.right)

        return left and right
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetry(root.left,root.right)