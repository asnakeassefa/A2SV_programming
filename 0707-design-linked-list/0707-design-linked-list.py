class Node:
    def __init__(self,value=0):
        self.value = value
        self.next = None
        
        
class MyLinkedList:
    
    def __init__(self):
        self.root = Node(0)
        self.count = 0
    
    def getNode(self,index):
        head = self.root
        i = 0
        while i < index:
            head = head.next
            i += 1
            
        return head
    def get(self, index: int) -> int:
        # print(self.count)
        if index >= self.count:
            return -1
        nodeVal = self.getNode(index)
        return nodeVal.value
    def addAtHead(self, val: int) -> None:
        dummy = Node(val)
        if self.count == 0:
            self.root = Node(val)
        else:
            dummy.next = self.root
            self.root = dummy
        self.count += 1
    def addAtTail(self, val: int) -> None:
        head = self.root
        dummy = Node(val)
        if self.count == 0:
            self.root = dummy
        else:
            while head and head.next:
                head = head.next
            head.next = dummy
        self.count += 1
        # print(self.count)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.count:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index < self.count:
            preNode = self.getNode(index - 1)
            newNode = Node(val)
            newNode.next = preNode.next
            preNode.next = newNode
            self.count += 1
    
    def deleteAtIndex(self, index: int) -> None:
        # self.p(self.root)
        if index == 0 and self.count > 0:
            self.root = self.root.next
            self.count -= 1
        elif index < self.count:
            newNode = self.getNode(index - 1)
            newNode.next = newNode.next.next
            self.count -= 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)