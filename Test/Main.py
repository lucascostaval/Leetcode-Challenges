class Solution:
    def getSum(self, a: int, b: int) -> int:
        s1 = "a"*a
        s2 = "a"*b
        return len("".join([s1, s2]))
    
print("a"*3)