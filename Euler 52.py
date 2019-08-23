
def mata_iste(cifra1, cifra2):
    for el in str(cifra1):
        if str(cifra1).count(el) != str(cifra2).count(el):
            return False
    return True

i = 1

testerji = [2, 3, 4, 5, 6]
nimamo =  True

while nimamo:
    nimamo = False
    for el in testerji:
        if not mata_iste(i, el*i):
            nimamo = True
    i += 1
print(i-1)


