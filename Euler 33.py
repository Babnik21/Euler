seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9] #opazimo, da ničle ne more imeti; če je v števcu 0 bo to trivial example ali pa ne bo moglo biti res

def okrajsaj(sez):      #pripravimo funkcijo za kasneje, sprejme seznam 2 intov: [števec, imenovalec]
    i = 2
    while i <= sez[0]:
        while sez[0] % i == 0 and sez[1] % i == 0:
            sez = [sez[0]//i, sez[1]//i]
        i += 1
    return sez

števci = []

for prva in seznam:
    for druga in seznam:
        števci += [10*prva + druga]

imenovalci = števci[::-1]    #reversano zaradi lažjega loopanja kasneje
print(imenovalci)
rezultat = []

for a in števci:         #kjer so a števci in b imenovalci
    for b in imenovalci:
        if a == b:      #če sta obe števki enaki imamo trivialen primer (zaradi tega reverse)
            break
        else:
            cifre_a = [a//10, a%10]         
            cifre_b = [b//10, b%10]
            if cifre_a[0] == cifre_b[1] and a/b == cifre_a[1]/cifre_b[0]:       
                rezultat += [[a, b]]
            elif cifre_a[1] == cifre_b[0] and a/b == cifre_a[0] / cifre_b[1]:      
                rezultat += [[a, b]]

stevec = 1
imenovalec = 1
for el in rezultat:
    stevec = stevec*el[0]
    imenovalec = imenovalec*el[1]

resitev = okrajsaj([stevec, imenovalec])
print(resitev[1])



    