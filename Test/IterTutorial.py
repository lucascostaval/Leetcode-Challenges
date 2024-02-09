lst = [1, 5, 2, 3]
for x in lst:
    print(x)
print("")

# How for x in is implemented
it = iter(lst)
while True:
    try:
        x = next(it)
        print(x) #do something
    except StopIteration:
        break


