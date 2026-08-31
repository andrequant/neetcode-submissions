class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        node = self.head.next
        for i in range(index):
            node = node.next
        return node.val
        

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        self.size +=1

    def addAtTail(self, val: int) -> None:
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = self.head
        for i in range(index):
            node = node.next
        new = ListNode(val)
        new.next = node.next
        node.next = new
        self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        node = self.head
        for i in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)