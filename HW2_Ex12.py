
summ = 4
mult = 4
for i in range(1000):
    for j in range(1000):
        if i + j == summ and i * j == mult:
            print(i, j)
