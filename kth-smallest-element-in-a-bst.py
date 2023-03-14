# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTravers(self,root,arr):
        if not root:
            return
        self.inorderTravers(root.left,arr)
        arr.append(root.val)
        self.inorderTravers(root.right,arr)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.inorderTravers(root,arr)
        return arr[k-1]