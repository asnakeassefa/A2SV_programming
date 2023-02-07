# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        slow = head
        pre = None
        
        for _ in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next
        if slow:
            if slow == head:
                head = head.next
            else:
                pre.next = slow.next
        return head