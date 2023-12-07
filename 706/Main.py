class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.h = 10000
        self.lst = [None]*self.h

    def put(self, key: int, value: int) -> None:
        hashKey = key%self.h
        previous = None
        current = self.lst[hashKey]
        while current is not None and current.key != key:
            previous = current
            current = current.next
        if previous is None and current is None:
            self.lst[hashKey] = ListNode(key, value)
        elif current is None:
            previous.next = ListNode(key, value)
        else:
            current.val = value

    def get(self, key: int) -> int:
        hashKey = key%self.h
        current = self.lst[hashKey]
        while current is not None and current.key != key:
            current = current.next
        getValue = -1
        if current is not None and current.key == key:
            getValue = current.val
        return getValue

    def remove(self, key: int) -> None:
        hashKey = key%self.h
        previous = None
        current = self.lst[hashKey]
        while current is not None and current.key != key:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self.lst[hashKey] = self.lst[hashKey].next
            else:
                previous.next = current.next