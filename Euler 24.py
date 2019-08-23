#lahko si pomagamo s številom premutacij in pogledamo, kam paše milijon-ta.
#prva desetina permutacij se začne z 0, naslednja z 1... tako naprej
#ko ugotovimo prvo števko postopek ponavljamo z naslednjo

sez = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
st = 999999    #ker je prva permutacija zares = 0, je 1000000. enaka 999999
resitev = []

def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n-1)

st_per = fakulteta(len(sez))

while len(sez) > 0:
    st_per = fakulteta(len(sez))
    en_kos = fakulteta(len(sez)-1)
    delitelj = st//en_kos
    st -= delitelj * en_kos
    resitev.append(sez[delitelj])
    sez.remove(sez[delitelj])


rezultat = ''.join(str(i) for i in resitev)
print(rezultat)

