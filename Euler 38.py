#n je lahko največ 5, za vsak n pa je število ustrezno veliko
#število je lahko največ 4-mestno, saj bi sicer že za n = 2 dobili 10 - mestno število

seznam = list(range(1, 10000))


def je_pan_9(cifra):
    if len(cifra) != 9:
        return False
    for el in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if str(el) not in cifra:
            return False
    return True

pandigiti = []

for el in seznam:
    i = 1
    niz = ''
    while len(niz) < 9:
        niz += str(i*el)
        i += 1
    if je_pan_9(niz):
        pandigiti.append(int(niz))

print(max(pandigiti))


