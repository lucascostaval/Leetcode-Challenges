class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        result = 0
        arr1, arr2 = [], []
        t1, t2 = uniqueCnt1, uniqueCnt2
        while uniqueCnt1 > 0 and uniqueCnt2 > 0:
            result += 1
            if result%divisor1 != 0: 
                uniqueCnt1 -= 1
                arr1.append(result)
            elif result%divisor2 != 0:
                uniqueCnt2 -= 1
                arr2.append(result)
        while uniqueCnt1 > 0:
            result += 1
            if result%divisor1 != 0:
                uniqueCnt1 -= 1
                arr1.append(result)
        while uniqueCnt2 > 0:
            result += 1
            if result%divisor2 != 0:
                uniqueCnt2 -= 1
                arr2.append(result)
        print(len(arr1), len(arr2))
        print(arr1, arr2)

        result = 0
        arr1, arr2 = [], []
        while t1 > 0 and t2 > 0:
            result += 1
            if result%divisor2 != 0: 
                t2 -= 1
                arr2.append(result)
            elif result%divisor1 != 0:
                t1 -= 1
                arr1.append(result)
        while t1 > 0:
            result += 1
            if result%divisor1 != 0:
                t1 -= 1
                arr1.append(result)
        while t2 > 0:
            result += 1
            if result%divisor2 != 0:
                t2 -= 1
                arr2.append(result)
        print(len(arr1), len(arr2))
        print(arr1, arr2)
        print()

        # result1 = 0
        # both_pass_1 = 0
        # t = uniqueCnt1+uniqueCnt2
        # while uniqueCnt1 > 0:
        #     result1 += 1
        #     if result1%divisor1 != 0 and result1%divisor2 != 0: both_pass_1 += 1
        #     if result1%divisor1 != 0: uniqueCnt1 -= 1
        # result2 = 0
        # both_pass_2 = 0
        # while uniqueCnt2 > 0:
        #     result2 += 1
        #     if result2%divisor1 != 0 and result2%divisor2 != 0: both_pass_2 += 1
        #     if result2%divisor2 != 0: uniqueCnt2 -= 1
        # both_pass = max(both_pass_1, both_pass_2)
        # print(result1, result2, both_pass)

        # result3 = 0
        # both_pass_3 = 0
        # while t > 0:
        #     result3 += 1
        #     if result3%divisor1 != 0 and result3%divisor2 != 0: both_pass_3 += 1
        #     t -= 1
        # print(result3, both_pass_3)
    
    def multiples_in_interval(self, a: int, b: int, d: int) -> int:
        a1, an = a, b
        while a1%d != 0: a1 += 1
        while an%d != 0: an -= 1
        return (an-a1)//d+1

    def lcm(self, a: int, b: int) -> int:
        gcd = self.euclid(a, b)
        return a*b//gcd
    
    def euclid(self, a: int, b: int) -> int:
        while b != 0: a, b = b, a%b
        return a


sol = Solution()
divisor1 = 19
divisor2 = 31
uniqueCnt1 = 41
uniqueCnt2 = 91
#print(sol.lcm(19, 31))
print(sol.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2))