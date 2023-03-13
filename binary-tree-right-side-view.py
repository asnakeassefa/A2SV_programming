# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travers(self,root,arr,store,d):
        if not root:
            return
        if not store.get(d):
            store[d] = True
            arr.append(root.val)
        self.travers(root.right,arr,store,d+1)
        self.travers(root.left,arr,store,d+1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        store = dict()
        self.travers(root,arr,store,0)
        return arr