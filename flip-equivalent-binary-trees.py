# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travers(self,root,parent,arr):
        if root and  not root.left and not root.right:
            arr[parent] = set()
        
        if root and root.left:
            arr[parent].add(root.left.val)
            self.travers(root.left,root.left.val,arr)
        if root and root.right:
            arr[parent].add(root.right.val)
            self.travers(root.right,root.right.val,arr)

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = defaultdict(set)
        arr2 = defaultdict(set)
        if root1:
            self.travers(root1,root1.val,arr1)
        if root2:
            self.travers(root2,root2.val,arr2)
        ans = True
        if len(arr1) != len(arr2):
            return False
        for key,val in arr1.items():
            if key not in arr2:
                ans = False
            for i in val:
                if i not in arr2[key]:
                    ans = False
                    break
            if not ans:
                break
        return ans