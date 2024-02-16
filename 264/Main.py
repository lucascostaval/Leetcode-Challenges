class Solution:
    def nthUglyNumber(self, n: int) -> int:
        number = 1
        lst_power_2 = []
        max_integer = 9223372036854775807
        while number <= max_integer:
            lst_power_2.append(number)
            number *= 2
        number = 1
        lst_power_3 = []
        while number <= max_integer:
            lst_power_3.append(number)
            number *= 3
        number = 1
        lst_power_5 = []
        while number <= max_integer:
            lst_power_5.append(number)
            number *= 5
        lst = []
        for i in range(len(lst_power_5)):
            for j in range(len(lst_power_3)):
                for k in range(len(lst_power_2)):
                    number = lst_power_5[i]*lst_power_3[j]*lst_power_2[k]
                    if number > max_integer: break
                    lst.append(number)
        lst.sort()
        return lst[n-1]


sol = Solution()
n = 11
print(sol.nthUglyNumber(n))
