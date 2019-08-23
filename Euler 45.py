def nti_triangle(n):
    return n*(n+1)//2
def dodaj_triangle(sez, n):
    return sez + [nti_triangle(n)]
def nta_penta(n):
    return n*(3*n - 1)//2
def dodaj_pento(sez, n):
    return sez + [nta_penta(n)]
def nta_hexa(n):
    return n*(2*n - 1)
def dodaj_hexo(sez, n):
    return sez + [nta_hexa(n)]

triangli = [1]
t = 2
pente = [1]
p = 2
hexe = [1]
h = 2
print(nti_triangle(3))

resitve = [0]
while resitve[-1] < 40756:
    if triangli[-1] <= pente[-1] and triangli[-1] <= hexe[-1]:
        triangli = dodaj_triangle(triangli, t)
        t += 1
    elif pente[-1] < triangli[-1] and pente[-1] <= hexe[-1]:
        pente = dodaj_pento(pente, p)
        p += 1
    elif hexe[-1] < triangli[-1] and hexe[-1] < pente[-1]:
        hexe = dodaj_hexo(hexe, h)
        h += 1
    if hexe[-1] == pente[-1] == triangli[-1]:
        i = hexe[-1]
        resitve.append(i)
        print(resitve)
        triangli = dodaj_triangle(triangli, t)
        t += 1
    print(resitve)



print(resitve[-1])




    