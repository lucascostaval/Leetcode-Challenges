class Solution:

    MOD = 1000000007

    def monkeyMove(self, n: int) -> int:
        return (self.power(2, n)-2)%self.MOD
    
    def power(self, a: int, n: int) -> int:
        if n == 0: return 1
        value = self.power(a, n//2)
        if n%2 == 1: return ((value*value)%self.MOD*a)%self.MOD
        return (value*value)%self.MOD