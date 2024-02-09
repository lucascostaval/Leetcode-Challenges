class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}
        for i in range(len(s)):
            if s[i] in h1 and h1[s[i]] != t[i] or t[i] in h2 and h2[t[i]] != s[i]: return False 
            h1[s[i]], h2[t[i]] = t[i], s[i]
        return True


s1 = "paper"
s2 = "title"
sol = Solution()
print(sol.isIsomorphic(s1, s2))