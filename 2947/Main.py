class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        tot = 0
        for i in range(len(s)):
            vowels = 0
            consonants = 0
            for j in range(i, len(s)):
                if s[j] in {"a", "e", "i", "o", "u"}: vowels += 1
                else: consonants += 1
                if consonants==vowels and (consonants*vowels)%k == 0: tot += 1
        return tot