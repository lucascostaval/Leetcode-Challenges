from typing import List

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result: List[str] = []
        primes = self.eratosthenes(101)
        for i in range(1, n):
            for j in range(i+1, n+1):
                isReduced: bool = True
                for x in primes:
                    if i%x == 0 and j%x == 0: isReduced = False
                if isReduced: result.append(f"{i}/{j}")
        return result
    
    def eratosthenes(self, n):
        if n < 2: return []
        is_prime = [True]*n
        for i in range(2, int(n**0.5)+1):
            for j in range(2*i, n, i): is_prime[j] = False
        return [x for x in range(2, n) if is_prime[x]]