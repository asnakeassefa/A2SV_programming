# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy2 = ListNode(0)
        curr = head
        start = None
        
        ptr = 1
        
        while ptr < left:
            start = curr
            curr = curr.next
            ptr += 1
        
        pre = None
        
        while curr and ptr <= right:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
            ptr += 1
        #asign startnode
        if start:
            start.next = pre
        else:
            start = pre
            head = start
        while pre and pre.next:
            pre = pre.next
        pre.next = curr
        return head