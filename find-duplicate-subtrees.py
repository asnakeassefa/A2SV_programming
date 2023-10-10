# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTree = defaultdict(list)
        ans = []
        def dfs(root):
            if not root:
                return " "
            temp = "|"
            temp += dfs(root.left) + str(root.val)
            temp += dfs(root.right)
            
            if temp in subTree:
                subTree[temp][0] += 1
            else:
                subTree[temp] = [1,root]
            return temp
        dfs(root)

        for key,[count,node] in subTree.items():
            if count > 1:
                ans.append(node)
        return ans