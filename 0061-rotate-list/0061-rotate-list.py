# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        first = head
        while first:
            length += 1
            first = first.next
        
        if length == k or length < 2:
            return head
        
        
        newLen = k % length
        if newLen == 0:
            return head
        
        
        fast = head
        slow = head
        
        for i in range(newLen):
            fast = fast.next
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # get first node
        
        newNode = slow.next
        lastNode = fast
        slow.next = None
        fast.next = dummy.next
        
        return newNode