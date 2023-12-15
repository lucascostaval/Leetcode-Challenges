class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] not in ('+', '-') and (ord(s[i]) < 48 or ord(s[i]) > 57):
            i += 1
        if i >= len(s):
            return 0
        negative = False
        if s[i] == '-':
            negative = True
            i += 1
        elif s[i] == '+':
            i += 1
        number_string = ""
        while i < len(s) and (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            number_string += s[i]
            i += 1
        limit = pow(2, 31)-1
        if negative:
            limit += 1
        number = 0
        weight = 1
        for n in range(len(number_string)-1, -1, -1):
            digit = int(number_string[n])
            number += digit*weight
            weight *= 10
            number = min(number, limit)
            if number == limit:
                break
        if negative:
            number *= -1
        return number

sol = Solution()
s = "words and 987"
n = sol.myAtoi(s)