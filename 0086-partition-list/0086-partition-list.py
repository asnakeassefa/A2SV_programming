# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy2 = ListNode(0)
        
        lessNode = ListNode(0)
        greater = ListNode(0)
        dummy.next = lessNode
        dummy2.next = greater
        while head:
            if head.val < x:
                lessNode.next = ListNode(head.val)
                lessNode = lessNode.next
            if head.val >= x:
                greater.next = ListNode(head.val)
                greater = greater.next
            head = head.next
        lessNode.next = dummy2.next.next
        
        return dummy.next.next