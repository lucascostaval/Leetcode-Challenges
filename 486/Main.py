from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.calculate_difference(nums) >= 0
    
    def calculate_difference(self, nums):
        if len(nums) == 0: return 0
        return max(nums[0]-self.calculate_difference(nums[1:]), nums[len(nums)-1]-self.calculate_difference(nums[:len(nums)-1]))
        

sol = Solution()
nums = [0,0,7,6,5,6,1]
print(sol.predictTheWinner(nums))    