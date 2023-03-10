# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == val:
            return root
        
        right = None
        left = None
        if root.val > val:
            left = self.searchBST(root.left,val)
        elif root.val < val:
            right = self.searchBST(root.right,val)
        if left:
            return left
        elif right:
            return right

        return