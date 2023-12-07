class ListNode:
    def __init__(self, value=0, next=None):
        self.value: int = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length: int = 0

    def appendRight(self, x: int) -> bool:
        newNode: ListNode = ListNode(x)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True
    
    def appendLeft(self, x: int) -> bool:
        newNode: ListNode = ListNode(x)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def popRight(self) -> ListNode:
        if self.length == 0:
            return None
        if self.length == 1:
            removed = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        previous = None
        current = self.head
        while current.next != None:
            previous = current
            current = current.next
        previous.next = None
        self.tail = previous
        self.length -= 1
        return current
    
    def popLeft(self) -> ListNode:
        if self.length == 0:
            return None
        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed
    
    def insert(self, x: int, index: int) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.appendLeft(x)
        if index == self.length:
            return self.appendRight(x)
        newNode: ListNode = ListNode(x)
        previous: ListNode = None
        current: ListNode = self.head
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = newNode
        newNode.next = current
        self.length += 1
        return True

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.popLeft()
        if index == self.length-1:
            return self.popRight()
        previous: ListNode = None
        current: ListNode = self.head
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = current.next
        self.length -= 1
        return current
    
    def remove(self) -> None:
        before = None
        current = self.head
        after = self.head
        while current != None:
            after = current.next
            current.next = before
            before = current
            current = after
        self.tail = self.head
        self.head = before

    def print(self) -> None:
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def makeEmpty(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> ListNode:
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def isEmpty(self):
        return self.length == 0
    
class Stack:
    def __init__(self):
        self.lst = LinkedList()

    def add(self, x: int) -> None:
        self.lst.appendLeft(x)
    
    def pop(self) -> int:
        if self.isEmpty():
            return -9999999
        node = self.lst.popLeft()
        return node.value
    
    def getSize(self) -> int:
        return self.lst.length
    
    def isEmpty(self) -> bool:
        return self.lst.isEmpty()
    
class Queue:
    def __init__(self):
        self.lst = LinkedList()

    def add(self, x: int) -> None:
        self.lst.appendRight(x)

    def pop(self) -> int:
        if self.isEmpty():
            return -9999999
        node = self.lst.popLeft()
        return node.value
    
    def getSize(self) -> int:
        return self.lst.length

    def isEmpty(self) -> bool:
        return self.lst.isEmpty()
    