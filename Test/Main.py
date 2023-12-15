class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_left(self, x: int) -> bool:
        new_node = ListNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def add_right(self, x: int) -> bool:
        new_node = ListNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_left(self) -> ListNode:
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
    
    def pop_right(self) -> ListNode:
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
        self.length -= 1
        return current
    
    def insert(self, x: int, index: int) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.add_left(x)
        if index == self.length:
            return self.add_right(x)
        new_node = ListNode(x)
        previous = None
        current = self.head
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = new_node
        new_node.next = current
        self.length += 1
        return True
    
    def remove(self, index: int) -> ListNode:
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_left()
        if index == self.length-1:
            return self.pop_right()
        previous = None
        current = self.head
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = current.next
        current.next = None
        self.length -= 1
        return current
    
    def get(self, index: int) -> ListNode:
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def reverse(self) -> None:
        if self.length == 0 or self.length == 1:
            return
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
    
    def is_empty(self):
        return self.length == 0
    
    def get_length(self):
        return self.length
    
class Queue:
    def __init__(self):
        self.lst = LinkedList()

    def add(self, x: int):
        self.lst.add_right(x)
    
    def pop(self) -> int:
        if self.is_empty():
            return -9999999
        removed_node = self.lst.pop_left()
        return removed_node.val
    
    def peek(self) -> int:
        if self.is_empty():
            return -9999999
        return self.lst.head.val
    
    def is_empty(self) -> bool:
        return self.lst.is_empty()
    
    def get_length(self) -> int:
        return self.lst.get_length()
    
class Stack:
    def __init__(self):
        self.lst = LinkedList()

    def add(self, x: int):
        self.lst.add_left()

    def pop(self) -> int:
        if self.is_empty():
            return -9999999
        removed_node = self.lst.pop_left()
        return removed_node.val
    
    def peek(self):
        if self.is_empty():
            return -999999
        return self.lst.head.val
    
    def is_empty(self) -> bool:
        return self.lst.is_empty()
    
    def get_length(self) -> int:
        return self.lst.get_length()