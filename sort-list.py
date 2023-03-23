# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,head1,head2):
        if not head1:
            return head2
        elif not head2:
            return head1
        if head1.val <= head2.val:
            head1.next = self.merge(head1.next,head2)
            return head1
        else:
            head2.next = self.merge(head1,head2.next)
            return head2
    def getMid(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return (head,temp)
    def mergeSort(self,head):
        if not head:
            return
        if head and not head.next:
            return head
        half = self.getMid(head)
        left = self.mergeSort(half[0])
        right = self.mergeSort(half[1])
        return self.merge(left,right)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)