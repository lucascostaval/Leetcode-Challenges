from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode: ListNode = None
        currentNode: ListNode = head
        while (currentNode != None):
            nextPrevious: ListNode = currentNode
            nextCurrent: ListNode = currentNode.next
            currentNode.next = previousNode
            previousNode = nextPrevious
            currentNode = nextCurrent
        return previousNode
    
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