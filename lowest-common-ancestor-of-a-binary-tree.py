# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def travers(self,root,p,q,ans):
        if ans[0]:
            return [True,True]
        if root and not root.left and not root.right:
            return [root == p,root == q]
        
        res1 = [False,False]
        res2 = [False,False]

        if root.left:
            res1 = self.travers(root.left,p,q,ans)
        if root.right:
            res2 = self.travers(root.right,p,q,ans)
            
        curr = [root == p,root == q]
        res = [res1[0] or curr[0],res1[1] or curr[1]]
        temp = [res[0] or res2[0],res[1] or res2[1]]
        if not ans[0] and temp == [True,True]:
            ans[1] = root
            ans[0] = True
        return temp
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [False,None]
        self.travers(root,p,q,ans)

        return ans[1]