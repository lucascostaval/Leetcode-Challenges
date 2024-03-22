from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        h = {}
        return self.calculate_difference(nums, h) >= 0
    
    def calculate_difference(self, nums, h):
        if len(nums) == 0: return 0
        if tuple(nums) in h: return h[tuple(nums)]
        value = max(nums[0]-self.calculate_difference(nums[1:], h), nums[len(nums)-1]-self.calculate_difference(nums[:len(nums)-1], h))
        h[tuple(nums)] = value
        return h[tuple(nums)]
        

sol = Solution()
nums = [0,0,7,6,5,6,1]
print(sol.predictTheWinner(nums))    