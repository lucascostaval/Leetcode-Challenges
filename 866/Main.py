from typing import List

class Solution:
    def primePalindrome(self, n: int) -> int:
        palindromes: List[str] = self.get_palindromes()
        palindromes_int: List[int] = [int(p) for p in palindromes if p[0] != "0"]
        for palindrome in palindromes_int:
            if self.is_prime(palindrome) and palindrome >= n: return palindrome
        return -1

    def get_palindromes(self) -> List[str]:
        dp: List[List[str]] = []
        dp.append([str(i) for i in range(10)])
        dp.append([str(i)+str(i) for i in range(10)])
        result: List[str] = dp[0]+dp[1]
        for i in range(2, 9):
            palindromes: List[str] = dp[i-2]
            current_result: List[str] = []
            for j in range(0, 10):
                for p in palindromes: current_result.append(str(j)+p+str(j))
            dp.append(current_result)
            result += current_result
        return result
    
    def is_prime(self, x: int) -> bool:
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x%i == 0: return False
        return True
    

sol = Solution()
n = 13
print(sol.primePalindrome(n))