from typing import List

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result: List[str] = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                a, b = j, i
                while b != 0: a, b = b, a%b
                if a == 1: result.append(f"{i}/{j}")
        return result


sol = Solution()
print(sol.simplifiedFractions(5))