class Node:
    def __init__(self, val: int, previous=None, next=None):
        self.val = val
        self.previous = previous
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def add_left(self, x: int) -> bool:
        new_node = Node(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def add_right(self, x: int) -> bool:
        new_node = Node(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def add_at(self, x: int, index: int) -> bool:
        if index < 0 or index > self.length: return False
        if index == 0: return self.add_left(x)
        if index == self.length: return self.add_right(x)
        new_node = Node(x)
        if index >= self.length//2:
            current = self.tail
            for _ in range(self.length-1-index): current = current.next
        else:
            current = self.head
            for _ in range(index): current = current.next
        previous: Node = current.previous
        previous.next = new_node
        new_node.previous = previous
        new_node.next = current
        current.previous = new_node
        self.length += 1
        return True
    
    def pop_left(self) -> Node:
        if self.length == 0: return None
        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        removed = self.head
        self.head = self.head.next
        self.head.previous = None
        self.length -= 1
        return removed
    
    def pop_right(self) -> Node:
        if self.length == 0: return None
        if self.length == 1:
            removed = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        removed = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        self.length -= 1
        return removed
    
    def pop_at(self, x: int, index: int) -> Node:
        if index < 0 or index >= self.length: return None
        if index == 0: return self.pop_left(x)
        if index == self.length-1: return self.pop_right(x)
        if index >= self.length//2:
            current = self.tail
            for _ in range(self.length-1-index): current = current.previous
        else:
            current = self.head
            for _ in range(index): current = current.next
        previous = current.previous
        after = current.next
        previous.next = after
        after.previous = previous
        self.length -= 1
        return current
    
    def get_left(self) -> Node:
        return self.head
    
    def get_right(self) -> Node:
        return self.tail
    
    def contains(self, value: int) -> bool:
        current = self.head
        while current is not None:
            if current.val == value: return True
            current = current.next
        return False

    def is_empty(self) -> bool:
        return self.length == 0
    
    def get_size(self) -> int:
        return self.length
    
    def __len__(self) -> int:
        return self.get_size()
    
    def __contains__(self, value: int) -> bool:
        return self.contains(value)
    
    def __str__(self) -> None:
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.val)
            current = current.next
        return str(lst)
    
    def __add__(self, other_ll):
        resulting_ll = LinkedList()
        head1: Node = self.head
        head2: Node = other_ll.head
        while head1 is not None:
            resulting_ll.add_right(head1.val)
            head1 = head1.next
        while head2 is not None:
            resulting_ll.add_right(head2.val)
            head2 = head2.next
        return resulting_ll
    

class MyCircularDeque:
    def __init__(self, k: int):
        self.ll = LinkedList()
        self.maximum_capacity = k

    def insertFront(self, x: int) -> bool:
        if self.isFull(): return False
        return self.ll.add_left(x)
    
    def insertLast(self, x: int) -> bool:
        if self.isFull(): return False
        return self.ll.add_right(x)
    
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.ll.pop_left()
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.ll.pop_right()
        return True
    
    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.ll.get_left().val
    
    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.ll.get_right().val

    def isFull(self) -> bool:
        return len(self.ll) == self.maximum_capacity
    
    def isEmpty(self) -> bool:
        return len(self.ll) == 0
    

myCircularDeque: MyCircularDeque = MyCircularDeque(3);
print(myCircularDeque.insertLast(1));  #// return True
print(myCircularDeque.insertLast(2));  #// return True
print(myCircularDeque.insertFront(3)); #// return True
print(myCircularDeque.insertFront(4)); #// return False, the queue is full.
print(myCircularDeque.getRear());      #// return 2
print(myCircularDeque.isFull());       #// return True
print(myCircularDeque.deleteLast());   #// return True
print(myCircularDeque.insertFront(4)); #// return True
print(myCircularDeque.getFront());     #// return 4