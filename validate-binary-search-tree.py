# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        self.arr.append(root.val)
        self.inOrder(root.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.arr = []
        self.inOrder(root)
        if self.arr == sorted(self.arr) and len(set(self.arr)) == len(self.arr):
            return True
        return False