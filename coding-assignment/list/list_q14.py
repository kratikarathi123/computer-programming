n = 2
for i in range(2 ** n):
    print(bin(i)[2:].zfill(n))
