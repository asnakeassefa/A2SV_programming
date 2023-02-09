# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = ListNode(0)
        dummy.next = ans
        pre = None
        
        while head:
            if head and head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                ans.next = ListNode(head.val)
                ans = ans.next
            head = head.next
        return dummy.next.next
            
                