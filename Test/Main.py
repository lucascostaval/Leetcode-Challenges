class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value: int):
        newNode: ListNode = ListNode(value)
        self.head: ListNode = newNode
        self.tail: ListNode = newNode
        self.length: int = 1
    
    def addRight(self, value: int) -> bool:
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
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
        removed = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        removed.prev = None
        self.length -= 1
        return removed
    
    def addLeft(self, value: int) -> bool:
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
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
        removed.next = None
        self.head.prev = None
        self.length -= 1
        return removed
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index > self.length//2:
            current = self.tail
            for _ in range(self.length-1-index):
                current = current.prev
        else:
            current = self.head
            for _ in range(index):
                current = current.next
        return current
    
    def set(self, index: int, value: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        node = self.get(index)
        node.value = value
        return True
    
    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.addLeft(value)
        if index == self.length:
            return self.addRight(value)
        new_node = ListNode(value)
        current: ListNode = self.get(index)
        previous: ListNode = current.prev
        previous.next = new_node
        new_node.prev = previous
        new_node.next = current
        current.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index: int) -> ListNode:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popLeft()
        if index == self.length-1:
            return self.popRight()
        removed = self.get(index)
        before: ListNode = removed.prev
        after: ListNode = removed.next
        before.next = after
        after.prev = before
        removed.prev = None
        removed.next = None
        self.length -= 1
        return removed
    
    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return
        second_node = self.head.next
        second_last_node = self.tail.prev
        tmp = self.head
        self.head = self.tail
        self.head.next = second_node
        self.head.prev = None
        second_node.prev = self.head
        self.tail = tmp
        self.tail.next = None
        self.tail.prev = second_last_node
        second_last_node.next = self.tail

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

ll = DoublyLinkedList(1)
for i in range(2, 3):
    ll.addRight(i)
ll.print_list()
print("")
ll.swap_first_last()
ll.print_list()