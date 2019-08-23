
dvice = []
trice = []
petke = []
sedmke = []
enajstke = []
trinajstke = []
sedmnajstke = []

for i in range(10, 1000):
    if i % 2 == 0:
        dvice.append(i)
    if i % 3 == 0:
        trice.append(i)
    if i % 5 == 0:
        petke.append(i)
    if i % 7 == 0:
        sedmke.append(i)
    if i % 11 == 0:
        enajstke.append(i)
    if i % 13 == 0:
        trinajstke.append(i)
    if i % 17 == 0:
        sedmnajstke.append(i)

def pocisti(sez):
    rezultat = []
    for el in sez:
        if len(str(el)) != 3:
            el = '0' + str(el)
        uredu = True
        for crka in str(el):
            if str(el).count(crka) != 1:
                uredu = False
        if uredu:
            rezultat.append(str(el))
    return rezultat

dvice = pocisti(dvice)
trice = pocisti(trice)
petke = pocisti(petke)
sedmke = pocisti(sedmke)
enajstke = pocisti(enajstke)
trinajstke = pocisti(trinajstke)
sedmnajstke = pocisti(sedmnajstke)

def pandigital(niz):
    for el in niz:
        if niz.count(el) != 1:
            return False
    return True

kandidati = []

for sedmnajstka in sedmnajstke:
    for trinajstka in trinajstke:
        if trinajstka[1:] != sedmnajstka[:-1]:
            continue
        else:
            for enajstka in enajstke:
                if enajstka[1:] != trinajstka[:-1]:
                    continue
                else:
                    for sedmka in sedmke:
                        if sedmka[1:] != enajstka[:-1]:
                            continue
                        else:
                            for petka in petke:
                                if petka[1:] != sedmka[:-1]:
                                    continue
                                else:
                                    for trica in trice:
                                        if trica[1:] != petka[:-1]:
                                            continue
                                        else:
                                            for dvica in dvice:
                                                if dvica[1:] == trica[:-1]:
                                                    cifra = dvica + trica[-1] + petka[-1] + sedmka[-1] + enajstka[-1] + trinajstka[-1] + sedmnajstka[-1]
                                                    kandidati += [cifra]

resni_kandidati = []

for el in kandidati:
    if pandigital(str(el)):
        resni_kandidati.append(el)

resitev = []
sample = '0123456789'

for el in resni_kandidati:
    for cifra in sample:
        if cifra not in el:
            resitev += [int(cifra + el)]
            break

print(sum(resitev))
