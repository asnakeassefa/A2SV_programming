# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLevel(self,root,d,arr):
        if not root:
            return
        arr[d].append(root.val)
        self.getLevel(root.left,d+1,arr)
        self.getLevel(root.right,d+1,arr)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = defaultdict(list)
        self.getLevel(root,0,arr)
        return [a for a in arr.values()]