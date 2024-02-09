from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maximum = 0
        for i in range(0, 10001):
            while height[left] < i:
                left += 1
                if left >= len(height): return maximum
            while height[right] < i:
                right -= 1
                if right < 0: return maximum
            h = i*(right-left)
            maximum = max(maximum, h)
        return maximum
    
    
sol = Solution()
height = [1,1]
print(sol.maxArea(height))