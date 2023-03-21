# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        que = deque()
        que.append((root,0))
        while que:
            ans = max(ans,((que[-1][1] - que[0][1]) + 1))
            i = 0
            length = len(que)
            while i < length:
                val = que.popleft()
                if val[0].left:
                    new1 = (2 * val[1]) + 1
                    que.append((val[0].left,new1))
                if val[0].right:
                    new2 = (2 * val[1]) + 2
                    que.append((val[0].right,new2))
                i += 1
        return ans