# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val = None
    def inOrder(self,root):
        if not root:
            return True
        left = self.inOrder(root.left)

        if self.val != None:
            if self.val >= root.val:
                return False
            self.val = root.val
        else:
            self.val = root.val
            
        right = self.inOrder(root.right)
        return right and left
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inOrder(root)