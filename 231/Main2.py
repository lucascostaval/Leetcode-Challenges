import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and abs(math.log2(n)-int(math.log2(n))) < 1e-20
    

sol = Solution()
n = 16
print(sol.isPowerOfTwo(n))