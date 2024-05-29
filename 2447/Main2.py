from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            gcd = 0
            for j in range(i, len(nums)):
                gcd = self.euclid(gcd, nums[j])
                if gcd == k: result += 1
        return result

    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a


sol = Solution()
nums = [4]
k = 7
print(sol.subarrayGCD(nums, k))