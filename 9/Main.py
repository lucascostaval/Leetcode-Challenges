from typing import List

class Solution:

    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        lst: List[int] = []
        while x > 0:
            lst.append(x%10)
            x //= 10
        left = 0
        right = len(lst)-1
        while left < right:
            if lst[left] != lst[right]:
                return False
            left += 1
            right -= 1
        return True

    

solution = Solution()
print(solution.isPalindrome(128921))
print(solution.isPalindrome(121))