# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        store = deque()
        store.append(root)
        dec = defaultdict(tuple)
        dec[root] = (0,0)

        while store:
            length = len(store)
            i = 0
            while i < length:
                val = store.popleft()
                if val.left:
                    store.append(val.left)
                    level = dec[val][0] + 1
                    left = dec[val][1] - 1
                    dec[val.left]= (level,left)
                if val.right:
                    store.append(val.right)
                    level = dec[val][0] + 1
                    left = dec[val][1] + 1
                    dec[val.right] = (level,left)
                i += 1
        dec = dict(sorted(dec.items(),key=lambda x:x[1][1]))
        newdict = defaultdict(list)
        ansdict = defaultdict(list)
        ans = []
        for key,val in dec.items():
            newdict[val].append(key.val)
        for key,val in newdict.items():
            ansdict[key[1]] += sorted(val)
        return [val for val in ansdict.values()]