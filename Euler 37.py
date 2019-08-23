
#opazimo, da soda števila ne morejo biti praštevila (razen 2, poseben primer, ki ga prištejemo kasneje)
#ker mora biti število praštevilo v vseh rotacijah, ne sme imeti sode števke

cifre = '123579'

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

seznam = range(1, 1000000, 1)

kandidati = []

for el in seznam:
    beseda = str(el)
    uredu = True
    if beseda[0] == '1' or beseda[-1] == '1' or '2' in beseda[1:] or beseda[-1] == '5' or beseda[-1] == '9' or beseda[0] == '9':
        uredu = False
    if uredu:
        for crka in beseda:
            if crka not in cifre:
                uredu = False
                break
    if uredu:
        kandidati += [el]

resitev = []

for el in kandidati:
    uredu = True
    if len(str(el)) == 1:
        uredu = False
    zacasno = el
    if uredu:               #krcimo v eno smer
        while len(str(zacasno)) != 1 and uredu:
            if prastevilo(zacasno):
                zacasno = zacasno//10
            else:
                uredu = False
    zacasno = el
    if uredu:
        while len(str(zacasno)) != 1 and uredu:
            if prastevilo(zacasno):
                zacasno = zacasno % (10 ** (len(str(zacasno)) - 1))
            else:
                uredu = False
    if uredu:
        resitev += [el]

print(sum(resitev))

        





