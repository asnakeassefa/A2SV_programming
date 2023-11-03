# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root and root.val == key:
            left = root.left
            if root.right:
                temp = root = root.right
                # temp = root.right
                while temp and temp.left:
                    temp = temp.left
                if temp:
                    temp.left = left
            else:
                root = root.left
            return root

        
        ans = root
        while root and root.val != key:
            parent = root
            if root.val > key:
                root = root.left
                if root and root.val == key:
                    if not root.left and not root.right:
                        parent.left = None
                    else:
                        left = root.left
                        if root.right:
                            parent.left = root.right
                            temp = root.right
                            while temp and temp.left:
                                temp = temp.left
                            if temp:
                                temp.left = left
                        else:
                            parent.left = left
            
            elif root.val < key:
                root = root.right
                # print(key)
                if root and root.val == key:
                    if not root.left and not root.right:
                        parent.right = None
                    else:
                        left = root.left
                        if root.right:
                            parent.right = root.right
                            temp = root.right
                            while temp and temp.left:
                                temp = temp.left
                            if temp:
                                temp.left = left
                        else:
                            parent.right = left
        return ans