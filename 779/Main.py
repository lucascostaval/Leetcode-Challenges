class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1
        if k == 0: return 0
        options = [[0, 1], [1, 0]]
        return options[self.kthGrammar(n, k//2+1)][k%2]


sol = Solution()
n = 2
k = 2