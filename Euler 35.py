#opazimo, da soda števila ne morejo biti praštevila (razen 2, poseben primer, ki ga prištejemo kasneje)
#ker mora biti število praštevilo v vseh rotacijah, ne sme imeti sode števke

cifre = '13579'

def prastevilo(n):
    if n <= 1:
        return False
    i = n**0.5
    if i == i//1:
        return False
    i = i //1
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True

def zarotiraj(niz):
    if len(niz) <= 1:
        return niz
    else:
        return niz[-1] + niz[:-1]

kombinacije = []

seznam = range(3, 1000000, 2)

kandidati = []

for el in seznam:
    beseda = str(el)
    uredu = True
    for crka in beseda:
        if crka not in cifre:
            uredu = False
            break
    if uredu:
        kandidati += [el]

rezultat = []

for el in kandidati:
    zacasno = str(el)
    uredu = True
    i = len(zacasno)
    while i > 0 and uredu:
        if not prastevilo(int(zacasno)):
            uredu = False
        else:
            zacasno = zarotiraj(zacasno)
        i -= 1
    if uredu:
        rezultat += [el]

print(len(rezultat) + 1)


        
    

