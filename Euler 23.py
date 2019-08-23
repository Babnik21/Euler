#drugi del ne gre s for loopom, ker preskakuje elemente
brez_abundantov = list(range(1,28124))

def vsota_del(n):
    if n == 1:
        return 0
    zacetna = int(n ** 0.5 // 1)
    vsota = 1
    if zacetna == n ** 0.5:
        vsota += zacetna
        zacetna -= 1
    while zacetna > 1:
        if n % zacetna == 0:
            vsota += zacetna + n//zacetna
        zacetna -= 1
    return vsota

abundanti = set()
for el in brez_abundantov:
    if vsota_del(el) > el:
        abundanti.add(el)

print(abundanti)
i = 1
while i <= 28123:
    for el in abundanti:
        if el > i:
            break
        elif i - el in abundanti:
            brez_abundantov.remove(i)
            break
    i += 1

print(sum(brez_abundantov))

