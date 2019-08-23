resitev = []

for i in range(1, 1000000):
    string = str(i)
    vsota = 0
    for el in string:
        vsota += (int(el))**5
    if vsota == i:
        resitev += [i]


print(sum(resitev) - 1)





