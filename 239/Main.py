import heapq

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, result = [], []
        h = {}
        for i in range(k):
            new_item = nums[i]*-1
            heapq.heappush(heap, new_item)
            if new_item in h:
                h[new_item] += 1
            else:
                h[new_item] = 1
        result.append(heap[0]*-1)
        for i in range(k, len(nums)):
            removed = nums[i-k]*-1
            if h[removed] > 0:
                h[removed] -= 1
            new_item = nums[i]*-1
            heapq.heappush(heap, new_item)
            if new_item in h:
                h[new_item] += 1
            else:
                h[new_item] = 1
            while h[heap[0]] <= 0: heapq.heappop(heap)
            result.append(heap[0]*-1)
        return result 