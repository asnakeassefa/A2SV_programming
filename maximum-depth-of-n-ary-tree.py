"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def DFS(self,root,depth,ans):
        if not root:
            return
        if not root.children:
            ans[0] = max(depth+1,ans[0])
            return
        for val in root.children:
            self.DFS(val,depth + 1,ans)
    def maxDepth(self, root: 'Node') -> int:
        ans = [0]
        self.DFS(root,0,ans)
        return ans[0]