from typing import List

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        largest = 0
        for i in range(len(nums)):
            if self.is_prime(nums[i][i]) and nums[i][i] > largest: largest = nums[i][i]
            if self.is_prime(nums[i][len(nums)-1-i]) and nums[i][len(nums)-1-i] > largest: largest = nums[i][len(nums)-1-i]
        return largest

    def is_prime(self, x: int) -> bool:
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x%i == 0: return False
        return True


sol = Solution()
nums = [[1,2,3],[5,17,7],[9,11,10]]
print(sol.diagonalPrime(nums))