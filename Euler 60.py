#Opazimo sledeče:
#4 od petih praštevil ki jih iščemo, morajo vsa biti oblike 3n + 1 ali vse oblike 3n + 2.
#Razlog: taki bosta tudi vsoti števk (za število tipa 3n + 1 bo tudi vsota števk 3k + 1)
#če bi 'concatenatali' števili tipa 3n + 1 in 3n + 2, bi bila vsota števk
#3k + 1 + 3m + 2 = 3(k + m + 1), kar je deljivo s 3 in zagotovo ne bo praštevilo
#edina izjema je praštevilo oblike 3n, ki zgoraj opisanega pogoja ne pokvari, na srečo pa obstaja le eno tako praštevilo: 3

def prastevilo(n):
    for i in range(1, int(n**0.5 // 1)):
        i += 1
        if n%i == 0:
            return False
    return True

print(prastevilo(4))