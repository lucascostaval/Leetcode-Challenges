from typing import List

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < len(nums) and not self.is_prime(nums[left]): left += 1
        while right >= 0 and not self.is_prime(nums[right]): right -= 1
        return right-left
    
    def is_prime(self, x: int) -> bool:
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x%i == 0: return False
        return True


sol = Solution()
nums = [2,6,3,4]
print(sol.maximumPrimeDifference(nums))