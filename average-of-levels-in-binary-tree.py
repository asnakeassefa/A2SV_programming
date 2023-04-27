# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root):
        visited = set([root])
        queue = deque([root])
        levels = []
        while queue:
            length = len(queue)
            temp = 0
            for i in range(length):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    visited.add(node.left)
                    queue.append(node.left)
                if node.right:
                    visited.add(node.right)
                    queue.append(node.right)
            levels.append(temp/length)
        return levels
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        return self.bfs(root)