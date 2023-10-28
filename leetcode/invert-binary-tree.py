# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)
            left = root.left
            right = root.right
            root.left = right
            root.right = left
        dfs(root)
        return root