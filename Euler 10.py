#naredimo seznam vseh lihih števil (vsa praštevila razen 2 so liha, 2 dodamo na koncu), nato pa brišemo ven vse večkratnike praštevil
#na koncu seštejemo vse elemente, ki so ostali na seznamu (vsa praštevila do 2000000)

omejitev = 2000000


seznam = set(range(3, omejitev, 2)) 

for cifra in range(3, int(omejitev ** 0.5) + 1):
    if cifra not in seznam:
        continue

    num = cifra
    while num < omejitev:
        num += cifra
        if num in seznam:
            seznam.remove(num)

print(2 + sum(seznam))
