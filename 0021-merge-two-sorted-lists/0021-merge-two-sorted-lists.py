# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = ListNode(0)
        dummy.next = head
        if list1 and list2:
            while list1 and list2:
                if list1.val > list2.val:
                    head.next = list2
                    head = head.next
                    list2 = list2.next
                else:
                    head.next = list1
                    head = head.next
                    list1 = list1.next
            if list1:
                head.next = list1
            if list2:
                head.next = list2
            return dummy.next.next
                
        else:
            if list1:
                return list1
            elif list2:
                return list2
            else:
                return list1