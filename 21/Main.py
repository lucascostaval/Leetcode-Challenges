from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = ListNode()
        tmp: ListNode = result
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                result.next = ListNode(list1.val)
                list1 = list1.next
            else:
                result.next = ListNode(list2.val)
                list2 = list2.next
            result = result.next
        while (list1 != None):
            result.next = ListNode(list1.val)
            list1 = list1.next
            result = result.next
        while (list2 != None):
            result.next = ListNode(list2.val)
            list2 = list2.next
            result = result.next
        return tmp.next
    
class Main:
    def main(self):
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(4)
        list2 = ListNode(1)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)
        solution = Solution()
        result = solution.mergeTwoLists(list1, list2)
        while result != None:
            print(result.val, end = " ")
            result = result.next

def run():
    mainObj = Main()
    mainObj.main()

if __name__ == "__main__":
    run()