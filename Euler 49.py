def permutacija(n1, n2, n3):
    for el in str(n1):
        if str(n1).count(el) != str(n2).count(el) or str(n1).count(el) != str(n3).count(el):
            return False
    return True

def prastevilo(n):
    i = n**0.5
    j = (n ** 0.5)//1
    if i == j or n == 1:
        return False
    while j > 1:
        if n%j == 0:
            return False
        j -= 1
    return True

def prastevila_do(n):
    if n == 3:
        return [3]
    else:
        i = 3
        sez = []
        while i < n:
            if prastevilo(i):
                sez += [i]
            i += 2
    return sez

sez = prastevila_do(10000)
prastevila = []

for el in sez:
    if el > 1000:
        prastevila.append(el)

indeks = 1
a = prastevila[indeks]
i = 1234


while indeks < len(prastevila) - 1:
    while a - i > 1000 and a + i < 10000:
        if (a + i) not in prastevila or (a - i) not in prastevila:
            i += 2
        elif permutacija(a, a+i, a-i):
            print(int(str(a-i) + str(a) + str(a+i)))
            break
        else:
            i += 2
    indeks += 1
    a = prastevila[indeks]
    i = 1234

