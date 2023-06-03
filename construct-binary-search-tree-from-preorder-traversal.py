# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getIndex(self,nums,val):
        j = 0
        for i,num in enumerate(nums):
            j += 1
            if num > val:
                return i
        return 101
    def travers(self,preorder,Tree):
        if not preorder:
            return None
        # if len(preorder) == 1:
        #     return TreeNode(preorder[0])
        Tree.val = preorder[0]
        index = self.getIndex(preorder,preorder[0])
        Tree.left = self.travers(preorder[1:index],TreeNode(0))
        Tree.right = self.travers(preorder[index:],TreeNode(0))

        return Tree

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        Tree = TreeNode(0)

        return self.travers(preorder,Tree)