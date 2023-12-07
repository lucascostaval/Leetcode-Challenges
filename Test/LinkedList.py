from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

class LinkedList:
    def __init__(self):
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length = 0

    def addLeft(self, x: int) -> bool:
        new_node = ListNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def addRight(self, x: int) -> bool:
        new_node = ListNode(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def popLeft(self) -> ListNode:
        if self.length == 0:
            return None
        if self.length == 1:
            removed: ListNode = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        removed: ListNode = self.head
        self.head = self.head.next
        self.length -= 1
        return removed
    
    def popRight(self) -> ListNode:
        if self.length == 0:
            return None
        if self.length == 1:
            removed: ListNode = self.tail
            self.head = None
            self.head = None
            self.length = 0
            return removed
        previous: ListNode = None
        current: ListNode = self.head
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
            return self.addLeft(x)
        if index == self.length:
            return self.addRight(x)
        new_node = ListNode(x)
        previous: ListNode = None
        current: ListNode = self.head
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = new_node
        new_node.next = current
        self.length += 1
        return True

    def remove(self, index: int) -> ListNode:
        if index < 0 or index >= self.length:
            return None
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

    def reverse(self) -> None:
        before: ListNode = None
        current: ListNode = self.head
        after: ListNode = self.head
        while current != None:
            after = current.next
            current.next = before
            before = current
            current = after
        self.tail = self.head
        self.head = before
    
    def get_by_index(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def get_length(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.length == 0
    
    def get_middle(self):
        if self.head is None or self.head.next is None:
            return self.head
        slow: ListNode = self.head
        fast: ListNode = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        if self.head is None or self.head.next is None:
            return False
        if self.head == self.head.next:
            return True
        slow: ListNode = self.head
        fast: ListNode = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_k_from_last(self, k: int):
        if k <= 0 or k > self.length:
            return None
        normalPointer: ListNode = self.head
        advantagePointer: ListNode = self.head
        for _ in range(k):
            advantagePointer = advantagePointer.next
        while advantagePointer is not None:
            normalPointer = normalPointer.next
            advantagePointer = advantagePointer.next
        return normalPointer
    
    def print_list(self):
        current: ListNode = self.head
        while current is not None:
            print(current.val)
            current = current.next

def create_list_by_array(arr: List[int]) -> ListNode:
    h = ListNode()
    tmp = h
    for x in arr:
        h.next = ListNode(x)
        h = h.next
    return tmp.next