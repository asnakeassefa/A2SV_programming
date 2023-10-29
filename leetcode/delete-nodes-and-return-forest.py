# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        ans = set()
        queue = deque()
        def dfs(root,got):
            if not root:
                return
            if got:
                return
            if root.val not in to_delete:
                queue.append(root)
                got = True
                return
            dfs(root.left,got)
            dfs(root.right,got)
        dfs(root,False)

        while queue:
            temp = queue.popleft()
            ans.add(temp)
            def dfs(temp):
                if not temp:
                    return
                dfs(temp.left)
                dfs(temp.right)
                if temp.left and temp.left.val in to_delete:
                    if temp.left.left:
                        queue.append(temp.left.left)
                    if temp.left.right:
                        queue.append(temp.left.right)
                    temp.left = None
                if temp.right and temp.right.val in to_delete:
                    if temp.right.left:
                        queue.append(temp.right.left)
                    if temp.right.right:
                        queue.append(temp.right.right)
                    temp.right = None
            dfs(temp)
        return ans