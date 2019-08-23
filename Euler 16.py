n = 2 ** 1000
vsota = 0

while n != 0:
    vsota += n%10
    n = (n - n%10)//10

print(vsota)


