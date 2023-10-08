# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travers(self,root,path,ans,p_sum,target):
        if not root:
            return
        if root and not root.left and not root.right:
            if root.val + p_sum == target:
                ans.append(path+[root.val])
            return
        self.travers(root.left,path + [root.val],ans,p_sum + root.val,target)
        self.travers(root.right,path + [root.val],ans,p_sum + root.val,target)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        self.travers(root,[],ans,0,targetSum)
        return ans