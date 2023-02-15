# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        pre = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
            
        stack = [0]
        ans = []
        while pre:
            while stack and pre.val >= stack[-1]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1])
            stack.append(pre.val)
            pre = pre.next
        return ans[::-1]
            