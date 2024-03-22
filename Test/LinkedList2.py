class Node:
    def __init__(self, val:int, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def add_front(self, x: int) -> bool:
        new_node = Node(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def add_last(self, x: int) -> bool:
        new_node = Node(x)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def add_at_index(self, x: int, index: int) -> bool:
        if index < 0 or index > self.length: return False
        if index == 0: return self.add_front(x)
        if index == self.length: return self.add_last(x)
        new_node = Node(x)
        previous: Node = None
        current: Node = self.head
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = new_node
        new_node.next = current

    def pop_front(self) -> Node:
        if self.length == 0: return None
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
    
    def pop_back(self) -> Node:
        if self.length == 0: return None
        if self.length == 1:
            removed = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        previous = self.head
        current = self.head
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        self.length -= 1
        return current
    
    def pop_at_index(self, index: int) -> Node:
        if index < 0 or index >= self.length: return None
        if index == 0: return self.pop_front()
        if index == self.length-1: return self.pop_back()
        previous = None
        current = self.head
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = current.next
        self.length -= 1
        return current

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
    
    def __contains__(self, value) ->  bool:
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
        head1 = self.head
        head2 = other_ll.head
        while head1 is not None:
            resulting_ll.add_last(head1.val)
            head1 = head1.next
        while head2 is not None:
            resulting_ll.add_last(head2.val)
            head2 = head2.next
        return resulting_ll

ll1 = LinkedList()
arr1 = [1, 4, 2, 9, -3, 2, -1, 5, 5, 2]
for x in arr1: ll1.add_front(x)
print(2 in ll1)
ll2 = LinkedList()
arr2 = [4, 2, -1]
for x in arr2: ll2.add_front(x)
ll3 = ll1+ll2
print(ll3)