class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length: return -1
        current = self.head
        for _ in range(index): current = current.next
        return current.val
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length: return
        if index == 0: self.addAtHead(val)
        elif index == self.length: self.addAtTail(val)
        else:
            new_node = Node(val)
            previous: Node = None
            current: Node = self.head
            for _ in range(index):
                previous = current
                current = current.next
            previous.next = new_node
            new_node.next = current
            self.length += 1

    def deleteAtHead(self) -> None:
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.length > 1:
            self.head = self.head.next
            self.length -= 1
        
    def deleteAtTail(self) -> None:
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.length > 1:
            previous: Node = self.head
            current: Node = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            self.length -= 1
            self.tail = previous
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length: return
        if index == 0: self.deleteAtHead()
        elif index == self.length-1: self.deleteAtTail()
        else:
            previous: Node = None
            current: Node = self.head
            for _ in range(index):
                previous = current
                current = current.next
            previous.next = current.next
            self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)