
def binary(n):
    if n == 0:
        return 0
    binarno = ''
    while n != 0:
        binarno = str(n%2) + binarno
        n = n // 2
    return binarno

def palindrom(niz):
    if len(niz) <= 1:
        return True
    elif niz[0] != niz[-1]:
        return False
    else:
        return palindrom(niz[1:-1])

vsota = 0

for i in range(1000001):
    if palindrom(str(i)) and palindrom(str(binary(i))):
        vsota += i

print(vsota)





