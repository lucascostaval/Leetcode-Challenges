class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.helper(n, k))
    
    def helper(self, n, k):
        k -= 1
        length_given_n = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]
        if k == 0: return 0
        if k == length_given_n[n]//2: return 1
        if k > length_given_n[n]//2: return abs(self.helper(n-1, 2*(length_given_n[n]//2)-k+1)-1)
        return self.helper(n-1, k+1)


sol = Solution()
n = 4
k = 1
for i in range(1, 16): print(sol.findKthBit(n, i))