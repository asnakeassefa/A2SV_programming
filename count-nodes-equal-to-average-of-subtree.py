# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def travers(self,root,arr):
        val1 = []
        val2 = []
        count = self.count
        if not root:
            return []
        arr[(root.val,count)].append(root.val)
        self.count += 1
        val1 += self.travers(root.left,arr)
        val2 += self.travers(root.right,arr)
        arr[(root.val,count)] += val1 + val2
        return arr[(root.val,count)]
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        arr = defaultdict(list)
        ans = 0
        self.travers(root,arr)
        print(arr)
        for key,val in arr.items():
            case = sum(val) // len(val)
            if key[0] == case:
                ans += 1
        return ans