import math

print(f"{3-0.5:.40f}")

n = 2097153
print(abs(int(math.log2(n))-math.log2(n)) < 1e-20)
print(abs(math.log2(n)-int(math.log2(n))) < 1e-20)
print(int(math.log2(n)), math.log2(n))