def factorial(n):       #ugotovimo, da je število lahko največ 7 mestno (7 * 9! je 7 mestno število, a ker je tudi 8*9! 7 mestno se ne bo izšlo)
    if n == 0:
        return 1
    rezultat = 1
    while n >= 1:
        rezultat = rezultat*n
        n -= 1
    return rezultat

seznam = []

for i in range(3, 3300000):
    zacasno = i
    vsota = 0
    while i != 0:
        vsota += factorial(i%10)
        i = i//10
    if vsota == zacasno:
        seznam += [vsota]

print(sum(seznam))

