#funkcija ni popolna ampak dovolj dobra
def deljenje_enke_na_n_mest(n, delj):
    i = 0
    rezultat = 0
    ostanek = 1
    while i <= n:
        if ostanek == 0:
            break
        elif delj > ostanek:
            ostanek = ostanek * 10
            rezultat = rezultat * 10
        else:
            rezultat = rezultat * 10 + ostanek // delj
            ostanek = (ostanek % delj)*10
        i += 1
    return(rezultat)

seznam = []

for i in range(1, 1001):                                    # upoštevamo, da število n ne more imeti periode daljše od n
    seznam += [[i, str(deljenje_enke_na_n_mest(2000, i))]]  # ker je naš največji n = 1000, bo 2000 vredu

def dolzina_periode(niz):
    i = 2
    j = 1
    if len(niz) <= 90:     # če ima manj kot toliko mest je končno št. decimalk => periode ni
        return 0
    while j < len(niz):
        i = 2
        while i < (len(niz)//2 - 1):
            if niz[:i] == niz[i:2*i]:
                return i
            else:
                i += 1
        niz = niz[1:]
    return None  #None uporabil med pisanjem, da sem preveril, če res potrebujem 2000 mest ali zadostuje kaj manj

dolzine = []

for el in seznam:
    dolzine += [[el[0], dolzina_periode(el[1])]]

najvecji = 0
najvecji_ost = 0
for el in dolzine:
    if el[1] > najvecji_ost:
        najvecji = el[0]
        najvecji_ost = el[1]

print(najvecji)




