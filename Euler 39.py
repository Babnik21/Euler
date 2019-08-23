#obstaja postopek za iskanje pitagorejskih trojk; po dolgem premisleku sem odkril metodo in jo uporabil

def je_trojka(a, b, c):
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2


trojke = []

n = 1
while n < 999:
    m = n + 1
    while 2* (m**2) + 2*m*n < 1001:
        a = m**2 - n **2
        b = 2 * m * n
        c = m**2 + n**2
        i = 1
        while a*i + b*i + c*i < 1001:
            if {a*i, b*i, c*i} not in trojke:
                trojke += [{a*i, b*i, c*i}]
            i += 1
        m += 1
    n += 1

i = 10
najvec = 0
zmagovalc = 0
while i < 1001:
    counter = 0
    for el in trojke:
        if sum(el) == i:
            counter += 1
    if counter > najvec:
        najvec = counter
        zmagovalc = i
    i += 1

print(zmagovalc)
    








