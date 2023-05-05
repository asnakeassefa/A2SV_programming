# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode(0)
        ans = ListNode(0,node)
        store = defaultdict(ListNode)
        nodes = []
        for i,value in enumerate(lists):
            store[i] = value
            if value:
                nodes.append([value.val,i])
        heapq.heapify(nodes)
        print(nodes)
        while nodes:
            value = heapq.heappop(nodes)
            node.next = ListNode(value[0])
            node = node.next
            store[value[1]] = store[value[1]].next
            recived = store[value[1]]
            if recived:
                heapq.heappush(nodes,[recived.val,value[1]])
        
        return ans.next.next