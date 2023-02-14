# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        MaxSum = 0
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        some = []
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            some.append(slow.val)
            slow = temp
        MaxSum = 0
        while head and pre:
            MaxSum = max(MaxSum,head.val + pre.val)
            head = head.next
            pre = pre.next
        
        return MaxSum
