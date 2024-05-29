from typing import List

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            lcm = 1
            for j in range(i, len(nums)):
                lcm = self.lcm(lcm, nums[j])
                if lcm == k: result += 1
                if lcm > k: break
        return result

    def lcm(self, a: int, b: int):
        gcd = self.euclid(a, b)
        return a*b/gcd

    def euclid(self, a: int, b: int):
        while b != 0: a, b = b, a%b
        return a
    

sol = Solution()
nums = [3]
k = 2
print(sol.subarrayLCM(nums, k))