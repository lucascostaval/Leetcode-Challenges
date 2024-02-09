class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class StackIterator:
    def __init__(self, head):
        self.head = head

    def __next__(self):
        if self.head is None:
            raise StopIteration
        else:
            n = self.head.val
            self.head = self.head.next
            return n

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def __iter__(self):
        return StackIterator(self.head)
    
    def __len__(self):
        return self.length
    
    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.val) + " "
            current = current.next
        result += "\n"
        return result

    def add(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.val
    
    def peek(self) -> int:
        if self.length == 0:
            return -1
        return self.head.val
    

stack = Stack()
stack.add(3)
stack.add(4)
stack.add(1)

for x in stack:
    print(x)

for x in stack:
    print(x)

print("")
print(stack)

lst = [1, 2, 3]
