from pyprimesieve import primes       #nima smisla se truditi s temi praštevili če jih lahko poiščemo na internetu

sez = primes(1000000)

i = 0
najdalsi = 21
zmagovalc = 0

while i + najdalsi < len(sez):
    j = najdalsi + i
    while sum(sez[i:j]) < sez[-1]:
        if sum(sez[i:j]) in sez and j > najdalsi:
            najdalsi = j - i
            zmagovalc = sum(sez[i:j])
        print(i, j, sum(sez[i:j]))
        j += 1
    i += 1

print(zmagovalc)


