import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and abs(math.log(n, 3)-round(math.log(n, 3))) < 1e-12