class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.h = 10000
        self.lst = [None for i in range(self.h)]

    def add(self, key: int) -> None:
        hashKey = key%self.h
        previous = None
        current = self.lst[hashKey]
        while current != None and current.val != key:
            previous = current
            current = current.next
        if previous == None and current == None:
            self.lst[hashKey] = ListNode(key)
        elif current == None:
            previous.next = ListNode(key)

    def remove(self, key: int) -> None:
        hashKey = key%self.h
        previous: ListNode = None
        current: ListNode = self.lst[hashKey]
        while current != None and current.val != key:
            previous = current
            current = current.next
        if current != None:
            if previous == None:
                self.lst[hashKey] = self.lst[hashKey].next
            else:
                previous.next = current.next

    def contains(self, key: int) -> bool:
        hashKey = key%self.h
        current = self.lst[hashKey]
        while current != None:
            if current.val == key:
                return True
            current = current.next
        return False