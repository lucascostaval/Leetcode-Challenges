class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]: j += 1
            elif j != 0: i, j = i-j, 0
            i += 1
            if j == len(needle): return i-j
        return -1


sol = Solution()
haystack = "leetcode"
needle = "leeto"
print(sol.strStr(haystack, needle))