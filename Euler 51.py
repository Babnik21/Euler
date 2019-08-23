from pyprimesieve import primes

def vstavi(st, cifra):     #stevilo vstavimo kot string
    resitev = ''
    for el in st:
        if el == '*':
            resitev += str(cifra)
        else:
            resitev += el
    return resitev

#iscemo stevilo, ki se konca z 1, 3, 7 ali 9, in ki vsebuje eno ali več ponovitev števila 0, 1, ali 2 (ker moramo najti število, ki bo praštevilo za 8 različnih cifer, vseh cifer pa je 10)
#zadnje stevilo zagotovo ne bo del ponovitve (saj so le 4 primeri kjer je število sploh lahko praštevilo, potrebujemo pa jih 8)

sez = primes(1000000)
preciscen = []
for el in sez:
    beseda = str(el)
    if '0' in beseda or '1' in beseda or '2' in beseda:
        preciscen.append(el)

#števila ne bodo nikoli deljiva z 2, ker zadnjo števko pustimo pri miru, lahko pa bi ob spreminjanju ene ali več števk postalo deljivo s 3
#da se to ne zgodi, mora biti vsota števk vedno ne-deljiva s 3;
#v začetnem praštevilu zagotovo ne bo deljiva s 3, poskrbeti pa moramo, da tudi potem ne bo. Ker potrebujemo kar 8 števil, je edina možnost,
#da spreminjamo po 3 števila (ne najdem načina, da bi ostanka enakih števk po deljenju s 3 ostajala enaka za vse možne cifre, če jih ni 3*n)
#upamo, da ni možno, da bi ostanek števk po deljenju s 3 alterniral le med 2 vrednostima izmed 3 možnih (načina ne najdem, če pa obstaja smo v zagati)
#iščemo prvo tako število, ki ustreza temu, poleg tega pa v 8 od 10 primerov ni deljivo s 5, 7, ... ostalimi praštevili

kandidati = []
for el in preciscen:
    niz = str(el)[:-1]
    slab = True
    for el1 in niz:
        if niz.count(el1) >= 3:      #morajo biti vsaj trije, ni pa nujno, da bomo spreminjali vse (v primeru da jih je več kot 3)
            slab = False            #najprej poskusimo, če je slučajno točno 3, sicer bomo dodali kodo če je večji od 3
    if not slab:
        kandidati.append(el)        #število kandidatov smo zdaj zmanjšali na manj kot 10%, zdaj bo najbrž računalnik lahko zmlel našo kodo

zmagovalec = 0

for el in kandidati:
    niz = str(el)
    razpolozljivi = niz[:-1]
    for el1 in razpolozljivi:
        if razpolozljivi.count(el1) == 3:       
            alfa = el1
    tester = ''
    for crka in razpolozljivi:
        if crka == alfa:
            tester += '*'
        else:
            tester += crka
    tester += niz[-1]
    counter = 0
    for i in range(0, 10):
        a = vstavi(tester, i)
        if int(a) in kandidati:
            counter += 1
    if counter == 8:
        zmagovalec = el
        break

print(zmagovalec)

