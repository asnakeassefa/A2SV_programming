# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,ans,arr,Sum,k):
        if not root:
            return
        Sum += root.val
        case = Sum - k
        ans[0] += arr[case]
        arr[Sum] += 1
        self.dfs(root.left, ans,arr,Sum, k)
        self.dfs(root.right, ans,arr,Sum, k)
        arr[Sum] -= 1
        Sum -= root.val
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = [0]
        arr = defaultdict(int)
        arr[0] = 1
        self.dfs(root,ans,arr,0,targetSum)
        return ans[0]