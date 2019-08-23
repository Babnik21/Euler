odpremo = open(r'C:\Users\jureb\OneDrive\Desktop\Euler\names.txt', 'r')
string = odpremo.read()
odpremo.close
string = string[1:-1]
sez = string.split('","')
sez.sort()

#do te točke samo importamo seznam, nič se ne zgodi

sample = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rezultat = 0
i = 1
for el in sez:
    score = i
    vsota = 0
    for crka in el:
        vsota += sample.index(crka)
    score = score * vsota
    rezultat += score
    i += 1
    
print(rezultat)



