tup = (1, 4, 9, 16, 25, 36,9, 49, 64, 81, 100)
x = 9
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("found", i)
        break
    i += 1