# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPath(self,root,val,arr):
        if root and not root.left and not root.right:
            arr.append(val+str(root.val))
        if not root:
            return
        value = val + str(root.val) + "->"
        self.getPath(root.left,value,arr)
        self.getPath(root.right,value,arr)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        self.getPath(root,"",arr)
        return arr