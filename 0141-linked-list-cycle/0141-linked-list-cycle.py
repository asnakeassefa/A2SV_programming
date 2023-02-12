# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        trace = defaultdict(int)
        
        while head:
            trace[head] += 1
            if trace[head] > 1:
                return True
            head = head.next
        return False