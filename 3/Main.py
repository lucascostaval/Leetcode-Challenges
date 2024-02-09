class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        current_size, maximum_size = 0, 0
        i = 0
        while i < len(s):
            if s[i] in h:
                maximum_size = max(maximum_size, current_size)
                current_size = 0
                i = h[s[i]]+1
                h = {}
            else:
                h[s[i]] = i
                current_size += 1
                i += 1
        return max(maximum_size, current_size)


s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))