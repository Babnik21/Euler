def naslednji_clen(n):
    if n%2 == 0:
        return n//2
    else: 
        return 3 * n + 1

def dolzina_zap(n):
    l = 0
    while n != 1:
        n = naslednji_clen(n)
        l += 1
    return l

najdaljsi = 0
najvecja_dolzina = 0
for i in range(1, 1000000):
    zacasno = dolzina_zap(i)
    if zacasno > najvecja_dolzina:
        najvecja_dolzina = zacasno
        najdaljsi = i

print(najdaljsi)


