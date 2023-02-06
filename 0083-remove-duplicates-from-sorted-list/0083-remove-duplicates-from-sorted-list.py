# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        pre = head
        if head:
            head = head.next
        while head:
            if pre.val != head.val:
                pre = head
                head = head.next
            elif pre.val == head.val:
                pre.next = head.next
                head = head.next
        return dummy.next