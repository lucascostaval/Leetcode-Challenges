from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_dist = 50
        number_of_ones = 0
        for i in range(len(nums)):
            n = nums[i]
            if nums[i] == 1: number_of_ones += 1
            for j in range(i, len(nums)):
                n = self.euclid(n, nums[j])
                if n == 1:
                    dist = j-i
                    if dist < min_dist: min_dist = dist
        if min_dist == 50: return -1
        elif number_of_ones == 0: return min_dist-1+len(nums)
        return len(nums)-number_of_ones
                        

    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a



sol = Solution()
nums = [1, 1]
print(sol.minOperations(nums))