
i = 1
cifra = ''

while len(cifra) < 1000001:
    cifra += str(i)
    i += 1

print(int(cifra[0]) * int(cifra[9]) * int(cifra[99]) * int(cifra[999]) * int(cifra[9999]) * int(cifra[99999]) * int(cifra[999999]))




