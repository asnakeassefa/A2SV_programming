# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sortedList = []
        while head:
            sortedList.append(head.val)
            head = head.next
        
        def getAns(val):
            print(val)
            if not val:
                return
            half = math.ceil(len(val) / 2) - 1
            root = TreeNode(val[half])
            root.left = getAns(val[:half])
            root.right = getAns(val[half+1:])
            return root
        return getAns(sortedList)