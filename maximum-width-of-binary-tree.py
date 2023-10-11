# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque([[root,0]])

        while queue:
            ans = max(ans,1+queue[-1][1]-queue[0][1])
            length = len(queue)
            for i in range(length):
                node,val= queue.popleft()
                
                if node.left:
                    curr_val = 2 * val + 1
                    queue.append([node.left,curr_val])
                if node.right:
                    curr_val = 2 * val + 2
                    queue.append([node.right,curr_val])
        return ans