# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        ans = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                ans += (',*')
                continue
            else:
                if ans:
                    ans += "," + str(node.val)
                else:
                    ans += str(node.val)
            queue.append(node.left)
            queue.append(node.right)
        return ans
    def deserialize(self, data):
        if not data:
            return
        data = list(data.split(','))
        length = len(data)
        ans = TreeNode(int(data[0]))
        queue = deque([ans])
        i = 1
        while queue:
            node = queue.popleft()
            if i < length and data[i] != "*":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if i < length and data[i] != "*":
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return ans

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))