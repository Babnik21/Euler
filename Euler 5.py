#ker potrebujemo le za števila do 20, za več ni smiselno

def na_prafaktorje(n):
    i = 2
    prafaktorji = []
    while n != 1:
        while n%i == 0:
            prafaktorji.append(i)
            n = n//i
        i += 1
    return prafaktorji

#z zgornjo funkcijo poiščemo prafaktorje vsake od prvih 20 števil in jih zapišemo v seznam (hitreje je na roke kot pisati program)
prafaktorji = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
rezultat = 1

for el in prafaktorji:
    rezultat = rezultat * el

print(rezultat)


