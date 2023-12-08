class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.head is None or self.head.next is None:
            return self.head
        firstNode = self.head
        lastFirstNode = None
        while firstNode.next is not None and firstNode.next.next is not None:
            secondNode = firstNode.next
            thirdNode = secondNode.next
            fourthNode = thirdNode.next
            secondNode.prev = lastFirstNode
            secondNode.next = firstNode
            firstNode.prev = secondNode
            if fourthNode is None:
                firstNode.next = thirdNode
            else:
                firstNode.next = fourthNode
            firstNode = thirdNode
        if firstNode.next is None:
            firstNode.prev = lastFirstNode
        else:
            secondNode = firstNode.next
            secondNode.prev = lastFirstNode
            secondNode.next = firstNode
            firstNode.prev = secondNode
            firstNode.next = None
        self.head = self.head.prev
        

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""