# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getParent(self,root,p,q):
        Max = max(p,q)
        Min = min(p,q)
        if root.val > p and root.val < q:
            return root
        elif root.val < p and root.val > q:
            return root
        elif root.val == p or root.val == q:
            print('root')
            return root
        elif Max < root.val:
            value = self.getParent(root.left,p,q)
            return value
        elif Min > root.val:
            value = self.getParent(root.right,p,q)
            return value
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.getParent(root,p.val,q.val)