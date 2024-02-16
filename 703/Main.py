from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        self.arr.sort()

    def add(self, val: int) -> int:
        index = 0
        self.arr.append(-1)
        while index < len(self.arr)-1 and val > self.arr[index]: index += 1
        for i in range(len(self.arr)-1, index, -1): self.arr[i] = self.arr[i-1]
        self.arr[index] = val
        return self.arr[len(self.arr)-self.k]

kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)
kthLargest.add(5)
kthLargest.add(10)
kthLargest.add(9)
kthLargest.add(4)