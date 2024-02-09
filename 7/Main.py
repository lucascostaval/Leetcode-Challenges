class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        maximum = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
        if not negative: maximum[len(maximum)-1] += 1
        number = []
        x = abs(x)
        while x > 0:
            number.append(x%10)
            x = x//10
        check1 = len(number) >= len(maximum)
        check2 = False
        for i in range(len(number)):
            if number[i] > maximum[i]:
                check2 = True
                break
            elif number[i] < maximum[i]: break
        extrapolate = check1 and check2
        if extrapolate: return 0
        result = 0
        potence = 1
        for i in range(len(number)-1, -1, -1):
            result += potence*number[i]
            potence *= 10
        if negative: return -result
        return result
        


sol = Solution()
x = -8463847412
print(sol.reverse(x))