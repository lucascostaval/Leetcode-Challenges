from typing import List

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x: int) -> None:
        self.heap.append(x)
        index = len(self.heap)-1
        while index > 0 and self.heap[index] < self.heap[(index-1)//2]:
            self.heap[index], self.heap[(index-1)//2] = self.heap[(index-1)//2], self.heap[index]
            index = (index-1)//2

    def remove(self) -> int:
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        removed = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sunk_down(0)
        return removed
    
    def sunk_down(self, index: int) -> None:
        min_index = index
        while True:
            left_index = index*2+1
            right_index = index*2+2
            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]: min_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]: min_index = right_index
            if index == min_index: return
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            index = min_index

    def __len__(self):
        return len(self.heap)

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap1, heap2 = MinHeap(), MinHeap()
        for x in nums1: heap1.insert(x)
        for x in nums2: heap2.insert(x)
        old_num1, old_num2 = heap1.remove(), heap2.remove()
        result = [(old_num1, old_num2)]
        k -= 1
        while k > 0:
            num1, num2 = heap1.remove(), heap2.remove()
            sum1 = old_num1+num2
            sum2 = old_num2+num1
            if sum1 < sum2:
                result.append((old_num1, num2))
                heap1.insert(num1)
            else:
                result.append((old_num2, num1))
                heap2.insert(num2)
            k -= 1
        return result


sol = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(sol.kSmallestPairs(nums1, nums2, k))