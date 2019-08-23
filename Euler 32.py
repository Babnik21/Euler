
def pandigital_devet(niz):
    if len(niz) != 9 or '0' in niz:
        return False
    for el in niz:
        if niz.count(el) != 1:
            return False
    return True

#ugotovimo, da je to mogoče le z produktom enomestne in 4-mestne ALI dvomestne in tromestne številke

resitev = []

for a in range(100):                #lahko se tako omejimo, če bi pustili a in b do 10000 bi
    for b in range(100,10000):      #preverjali vsak produkt 2x (saj je a*b = b*a)
        if a*b >= 10000:
            break
        elif pandigital_devet(str(a) + str(b) + str(a*b)) and a*b not in resitev:
            resitev += [a*b]

print(sum(resitev))



