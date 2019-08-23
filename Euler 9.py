from math import sqrt

def trojka_za(a, b):
    if sqrt(a ** 2 + b ** 2) == sqrt(a ** 2 + b ** 2)//1:
        return sqrt(a ** 2 + b ** 2)//1
    else: 
        return 0


resitev = 0
seznam = []

for i in range(1, 500):
    for j in range(1, 500):
        a = trojka_za(i, j)
        if a + i + j == 1000 and a != 0:
            resitev = a*i*j
            break

print(int(resitev))