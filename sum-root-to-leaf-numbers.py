# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,ans,temp):
        if root and not root.left and not root.right:
            temp += str(root.val)
            ans.append(temp)
            return
        if root and root.left:
            self.DFS(root.left,ans,temp+ str(root.val))
        if root and root.right:
            self.DFS(root.right,ans,temp+ str(root.val))
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        self.DFS(root,ans,"")
        res = 0
        print(ans)
        for val in ans:
            res += int(val)
        return res