# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMode(self,root,ans):
        if not root:
            return
        ans[root.val] += 1
        self.getMode(root.left,ans)
        self.getMode(root.right,ans)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)
        self.getMode(root,ans)
        Max = max(ans.values())
        res = []
        for key,val in ans.items():
            if val == Max:
                res.append(key)
        return res