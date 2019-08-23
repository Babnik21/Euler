#program ne zmelje za 9-mestna števila, imeli smo malo sreče

def je_pandigital(n):
    sez = '123456789'
    model = sez[:len(str(n))]
    for el in model:
        if str(n).count(el) != 1:
            return False
    return True

def prastevilo(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def vsota_stevk(n):
    if n == 0:
        return 0
    else:
        return n%10 + vsota_stevk(n//10)

pandigiti = []

for el in range(9999999, 1, -2):
    if je_pandigital(el):
        pandigiti.append(el)

print(pandigiti)

for el in pandigiti:
    if prastevilo(el):
        print(el)
        break




