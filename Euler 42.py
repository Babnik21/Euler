
odpremo = open(r'C:\Users\jureb\OneDrive\Desktop\Euler\words.txt', 'r')
string = odpremo.read()
odpremo.close()
string = string[1:-1]
sez = string.split('","')
sez.sort()

#do tu samo importamo seznam

#preverimo dolžine
maxi = 0
for el in sez:
    maxi = max(len(el), maxi)

#najdaljša beseda je dolga 14 črk, torej bodo zagotovo vse vrednosti pod 26*14, potrebujemo triangle števila do 26*14

def trikotnik(n):
    return n*(n+1)//2

triangles = [0]  #damo noter 0 zaradi index errorja, kasneje jo odstranimo
i = 1
while triangles[-1] < 26 * 14:
    triangles.append(trikotnik(i))
    i += 1
triangles.remove(0)

sample = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rezultat = 0
for el in sez:
    vsota = 0
    for crka in el:
        vsota += sample.index(crka)
    if vsota in triangles:
        rezultat += 1

print(rezultat)

