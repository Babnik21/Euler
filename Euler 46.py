
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

#ker iscemo samo liha stevila lahko ignoriramo 2, ceprav je prastevilo

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

def prafaktorji(n):
    i = 2
    sez = []
    while n != 1:
        while n%i == 0:
            n = n//i
            sez += [i]
        if i == 2:
            i += 1
        else:
            i += 2
    return sez

def je_kvadrat(n):
    sez = prafaktorji(n)
    for el in sez:
        if sez.count(el) % 2 != 0:
            return False
    return True


osnova = list(range(33, 10000, 2))
zacasno = list(range(33, 10000, 2))
prastevila = prastevila_do(10000)

for el in osnova:
    i = 0
    j = el
    uredu = True
    while prastevila[i] < j and uredu:
        if je_kvadrat((el-prastevila[i])//2):
            zacasno.remove(el)
            uredu = False
        i += 1

for el in zacasno:
    if not prastevilo(el):
        print(el)
        break

#malo srece da je rezultat majhen, sicer bi imeli tezave, ker bi racunalnik mlel predolgo.



