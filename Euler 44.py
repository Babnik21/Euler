
def nta_penta(n):
    return n*( 3 * n - 1)//2

def pente_do(n, od = 1):
    sez = []
    for i in range(od, n + 1):
        sez.append(nta_penta(i))
    return sez

def dodaj_pento(sez, n):
    return sez + [nta_penta(n)]

seznam = pente_do(500)
i = 501
razlike = []
nadaljuj = True
resitev = []

while nadaljuj:
    seznam = dodaj_pento(seznam, i)
    i += 1
    for el in seznam[:-1]:
        if seznam[-1] - el in seznam:
            razlike += [[seznam[-1], el]]
    for el in razlike:
        if el[1] + el[0] in seznam:
            nadaljuj = False
            resitev = el
        elif seznam[-1] > el[0] + el[1]:
            razlike.remove(el)

print(abs(resitev[0] - resitev[1]))












