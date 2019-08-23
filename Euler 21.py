def vsota_pravih_del(n):
    i = n//2 + 1
    vsota = 0
    while i > 0:
        if n % i == 0:
            vsota += i
        i -= 1
    return vsota

vsota = 0
j = 1
while j < 10000:
    k = vsota_pravih_del(j)
    if vsota_pravih_del(k) == j and k < 10000 and j != k:
        vsota += j
    j += 1

print(vsota)







