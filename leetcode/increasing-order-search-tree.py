# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def dfs(self,root,arr):
        if not root:
            return
        self.dfs(root.left,arr)
        arr.append(root.val)
        self.dfs(root.right,arr)
    def build(self,arr,i):
        if i >= len(arr):
            return
        root = TreeNode(arr[i])
        root.right = self.build(arr,i+1)
        return root
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.dfs(root,arr)
        return self.build(arr,0)
