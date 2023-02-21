# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        iterator = head
        count = 0
        while iterator:
            count += 1
            iterator = iterator.next
        if not head:
            return None
        lastOdd = None
        if head:
            odd = head
            even = head.next
            evenStart = head.next
        if count % 2 != 0:
            while odd and even:
                odd.next = even.next
                odd = odd.next
                if odd:
                    even.next = odd.next
                    even = even.next
        elif count % 2 == 0:
            while odd and even:
                odd.next = even.next
                lastOdd = odd
                odd = odd.next
                if odd:
                    even.next = odd.next
                    even = even.next
            odd = lastOdd
        if odd and evenStart:
            odd.next = evenStart
        return dummy.next