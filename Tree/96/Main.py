class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0 for i in range(20)]
        memo[0] = 1
        memo[1] = 1
        for m in range(2, 20):
            tot = 0
            for rootVal in range(1, m+1):
                tot += memo[rootVal-1]*memo[m-rootVal]
            memo[m] = tot
        return memo[n]
