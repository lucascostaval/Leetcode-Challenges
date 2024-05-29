from typing import Tuple, List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1: return 0
        stockPrices.sort()
        current_difference_tuple: Tuple[int, int] = self.reduce((stockPrices[1][1]-stockPrices[0][1]), (stockPrices[1][0]-stockPrices[0][0]))
        count = 1
        for i in range(2, len(stockPrices)):
            difference = self.reduce((stockPrices[i][1]-stockPrices[i-1][1]),(stockPrices[i][0]-stockPrices[i-1][0]))
            if difference != current_difference_tuple:
                count += 1
                current_difference_tuple = difference
        return count
    
    def reduce(self, a: int, b: int) -> Tuple[int, int]:
        gcd = self.euclid(a, b)
        return (a//gcd, b//gcd)

    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a

        

sol = Solution()
stockPrices = [[3,4],[1,2],[7,8],[2,3]]
print(sol.minimumLines(stockPrices))
