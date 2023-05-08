# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildDict(self,root,store):
        if root and not root.left and not root.right:
            return
        if root and root.left:
            store[root.val].append(root.left.val)
            store[root.left.val].append(root.val)
            self.buildDict(root.left,store)
        if root and root.right:
            store[root.val].append(root.right.val)
            store[root.right.val].append(root.val)
            self.buildDict(root.right,store)

    def bfs(self,store,target,k):
        visited = set([target])
        queue= deque([target])
        count = 0
        ans = []
        while queue:
            length = len(queue)
            
            if k == 0:
                return list(queue)
            for _ in range(length):
                node = queue.popleft()
                for val in store[node]:
                    if val not in visited:
                        queue.append(val)
                        visited.add(val)
            k -= 1
        return ans
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        store = defaultdict(list)
        self.buildDict(root,store)
        
        return self.bfs(store,target.val,k)