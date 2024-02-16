from typing import List

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x: int) -> None:
        self.heap.append(x)
        index = len(self.heap)-1
        while index > 0 and self.heap[index] > self.heap[(index-1)//2]:
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
        max_index = index
        while True:
            left_index = index*2+1
            right_index = index*2+2
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]: max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]: max_index = right_index
            if max_index == index: return
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index

class Node:
    def __init__(self, val: List[int], next=None):
        self.val = val
        self.next = next

class Map:
    def __init__(self):
        self.arr = [[] for i in range(503)]

    def insert(self, key: int, value: List[int]) -> None:
        k = key%len(self.arr)
        self.arr[k].append([key, value])
    
    def get(self, key) -> List[int]:
        k = key%len(self.arr)
        lst = self.arr[k]
        for pair in lst:
            if pair[0] == key: return pair[1]
        return None
    
    def __contains__(self, key):
        return self.get(key) != None
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        return self.insert(key, value)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        h = Map()
        current_number = nums[0]
        start_index = 0
        heap = MaxHeap()
        for i in range(len(nums)):
            if nums[i] != current_number:
                frequency = i-start_index
                if frequency in h: h[frequency].append(current_number)
                else: 
                    h[frequency] = [current_number]
                    heap.insert(frequency)
                start_index = i
                current_number = nums[i]
        frequency = len(nums)-start_index
        if frequency in h: h[frequency].append(current_number)
        else: 
            h[frequency] = [current_number]
            heap.insert(frequency)
        result = []
        while k > 0:
            lst = h[heap.remove()]
            for x in lst:
                result.append(x)
                k -= 1
                if k <= 0: break
        return result
                

sol = Solution()
nums = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
k = 3
print(sol.topKFrequent(nums, k))