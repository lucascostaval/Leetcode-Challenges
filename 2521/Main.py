from typing import Set, List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s: Set[int] = set()
        for x in nums:
            primes: List[int] = self.get_unique_primes(x)
            for p in primes: s.add(p)
        return len(s)

    def get_unique_primes(self, x: int) -> List[int]:
        if x < 2: return []
        i = 2
        result = []
        while x > 1:
            if x%i == 0 and self.is_prime(i):
                result.append(i)
                while x%i == 0: x //= i
            i += 1
        return result

    def is_prime(self, x: int) -> bool:
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x%i == 0: return False
        return True

sol = Solution()
nums = [2, 4, 8, 16]
print(sol.distinctPrimeFactors(nums))