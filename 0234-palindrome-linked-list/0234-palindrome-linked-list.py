# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        pre = None
        fast = head
        count = 0
        while fast and fast.next:
            count += 2
            fast = fast.next.next
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        # check count is odd or not
        if fast:
            slow = slow.next
        while pre and slow:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next
        return True