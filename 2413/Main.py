class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n+n*(n%2 != 0)