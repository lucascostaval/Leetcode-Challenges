from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        h = {}
        for card in deck:
            if card in h: h[card] += 1
            else: h[card] = 1
        minimum_count = min(list(h.values()))
        primes: List[int] = self.find_primes(minimum_count)
        for p in primes:
            for card in deck:
                if h[card]%p != 0: break
            else: return True
        return False
        
    def find_primes(self, x: int) -> List[int]:
        result: List[int] = []
        i = 2
        while x > 1:
            if self.is_prime(i):
                if x%i == 0: result.append(i)
                while x%i == 0: x //= i
            i += 1
        return result

    def is_prime(self, n: int) -> bool:
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0: return False
        return True
    

sol = Solution()
deck = [1,1,1,2,2,2,3,3]
print(sol.hasGroupsSizeX(deck))