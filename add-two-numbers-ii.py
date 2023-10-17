# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre1 = None
        pre2 = None

        while l1:
            temp = l1.next
            l1.next = pre1
            pre1 = l1
            l1 = temp
        
        while l2:
            temp = l2.next
            l2.next = pre2
            pre2 = l2
            l2 = temp
        temp = 0
        head = ListNode(0)
        nextNode = head
        while pre1 and pre2:
            val = str(pre1.val + pre2.val + temp)
            pre1 = pre1.next
            pre2 = pre2.next
            temp = 0
            nextNode.next = ListNode(int(val[-1]))
            nextNode = nextNode.next
            if len(val) == 2:
                # if not pre1 and not pre2:
                #     temp = int(val)
                # else:
                temp = int(val[0])

        print(temp)
        while pre1:
            val = str(pre1.val + temp)
            temp = 0
            pre1 = pre1.next
            nextNode.next = ListNode(int(val[-1]))
            nextNode = nextNode.next
            if len(val) == 2:
                temp = int(val[0])
        while pre2:
            val = str(pre2.val + temp)
            pre2 = pre2.next
            nextNode.next = ListNode(int(val[-1]))
            nextNode = nextNode.next
            temp = 0
            if len(val) == 2:
                temp = int(val[0])
        if temp:
            val = str(temp)
            for i in range(len(val)-1,-1,-1):
                nextNode.next = ListNode(int(val[i]))
                nextNode = nextNode.next
            temp = 0
        head = head.next
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre