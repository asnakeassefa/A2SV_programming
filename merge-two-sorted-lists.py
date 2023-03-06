# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMin(self, list1,list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.getMin(list1.next,list2)
            return list1
        else:
            list2.next = self.getMin(list1,list2.next)
            return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = self.getMin(list1,list2)
        return dummy.next