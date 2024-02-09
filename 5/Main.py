class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_left, long_right = -1, -1
        maximum = -1
        values = []
        for i in range(len(s)): values.append((i, i))
        for i in range(len(s)-1): values.append((i, i+1))
        for value in values:
            left, right = value
            while left >= 0 and right < len(s) and s[left] == s[right]: left, right = left-1, right+1
            if right-left+1 > maximum:
                maximum = right-left+1
                long_left, long_right = left+1, right-1
        return s[long_left:long_right+1]


s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))