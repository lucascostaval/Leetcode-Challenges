s = "Yellow Yaks like yelling and yawning and yes....turday they yodled while eating yuky yams"
lst = [c for c in s if c.upper() not in ("A", "B", "C", "D", "E", " ") and c.upper() in list(map(chr, range(65, 91)))]
print(lst)