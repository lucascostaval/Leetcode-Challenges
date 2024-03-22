class Solution:

    MOD = 1000000007

    def countGoodNumbers(self, n: int) -> int:
        times_to_power_5 = n//2
        times_to_power_4 = n//2
        if n%2 == 1: times_to_power_5 += 1
        power_5 = self.power(5, times_to_power_5)%self.MOD
        power_4 = self.power(4, times_to_power_4)%self.MOD
        return (power_5*power_4)%self.MOD

    def power(self, a: int, n: int) -> int:
        if n == 0: return 1
        value = self.power(a, n//2)
        if n%2 == 1: return (((value*value)%self.MOD)*a)%self.MOD
        return (value*value)%self.MOD