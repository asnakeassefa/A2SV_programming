# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = 0
        def inorderTravers(root):
            if not root:
                return
            inorderTravers(root.left)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
            inorderTravers(root.right)
        inorderTravers(root)
        return self.res