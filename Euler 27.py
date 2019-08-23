#pri pouku na vajah smo definirali funkcije za iskanje praštevil do n, to uporabimo
#opazimo, da mora biti b praštevilo, saj bo le tedaj 0**2 + a * 0 + b praštevilo, in vedno bo + b (nikoli - b)

def je_deljivo_s_katerim_od(n, seznam):
    if seznam == []: 
        return False 
    else: 
        return n % seznam[0] == 0 or je_deljivo_s_katerim_od(n, seznam[1:])

def prastevila_do(n): 
    if n <= 1: 
        return [] 
    manjsa_prastevila = prastevila_do(n - 1) 
    if je_deljivo_s_katerim_od(n, manjsa_prastevila): 
        return manjsa_prastevila 
    else: 
        return manjsa_prastevila + [n]

def je_prastevilo(n): 
    if n <= 1: 
        return False 
    else: 
        prastevila = prastevila_do(round(n ** 0.5)) 
        return not je_deljivo_s_katerim_od(n, prastevila)

prastevila = prastevila_do(997) #do 1000 ne gre (max recursion depth exceeded) od 997 in 1000 pa ni praštevila tako da je vseeno
kandidati_a = list(range(1001))

counter_zm = 0
zmagovalna = [0, 0]

for b in prastevila:
    for a in kandidati_a:
        counter = 0
        n = 0
        while je_prastevilo(n**2 + a*n + b):
            n += 1
            counter += 1
        if counter > counter_zm:
            counter_zm = counter
            zmagovalna = [a, b]
        counter = 0
        n = 0
        while je_prastevilo(n**2 - a*n + b):
            n += 1
            counter += 1
        if counter > counter_zm:
            counter_zm = counter
            zmagovalna = [-a, b]

print(zmagovalna[0] * zmagovalna[1])

a = zmagovalna[0]
b = zmagovalna[1]
counter = 0
n = 0
while je_prastevilo(n**2 + a*n + b):
    n += 1
    counter += 1

print(counter)








