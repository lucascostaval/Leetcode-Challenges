from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes: List[int] = self.eratosthenes(left, right+1)
        if len(primes) < 2: return [-1, -1]
        min_dist = primes[1]-primes[0]
        a, b = primes[0], primes[1]
        for i in range(2, len(primes)):
            if primes[i]-primes[i-1] < min_dist:
                min_dist = primes[i]-primes[i-1]
                a, b = primes[i-1], primes[i]
        return [a, b]

    def eratosthenes(self, a: int, b: int) -> List[int]:
        if b < 2: return []
        is_prime: List[bool] = [True]*b
        for i in range(2, int(b**0.5)+1):
            for j in range(2*i, b, i): is_prime[j] = False
        return [x for x in range(max(2, a), b) if is_prime[x]]


sol = Solution()
left = 4
right = 6
print(sol.closestPrimes(left, right))