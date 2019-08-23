slovar = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}
def povelikosti(sez):
    seznam = []
    for el in sez:
        seznam.append(slovar[el[0]])
    seznam.sort(reverse = True)
    return seznam

def je_barva(sez):
    barva = sez[0][1]
    for el in sez:
        if el[1] != barva:
            return False
    return True

def je_lestvica(sez):
    seznam = []
    for el in sez:
        seznam.append(slovar[el[0]])
    seznam.sort()
    for el in seznam:
        if seznam.count(el) != 1:
            return False
    i = 0
    while i < 4:
        if seznam[i] + 1 != seznam[i + 1]:
            return False
        i += 1
    return True

def je_poker(sez):
    seznam = []
    for el in sez:
        seznam.append(slovar[el[0]])
    for el1 in seznam:
        if seznam.count(el1) == 4:
            return True
    return False

def je_tris(sez):
    seznam = []
    for el in sez:
        seznam.append(slovar[el[0]])
    for el1 in seznam:
        if seznam.count(el1) == 3:
            return True
    return False

def je_par(sez):
    seznam = []
    for el in sez:
        seznam.append(slovar[el[0]])
    for el1 in seznam:
        if seznam.count(el1) == 2:
            return True
    return False

def straight_flush(sez):
    if je_barva(sez) and je_lestvica(sez):
        return True
    else:
        return False

def royal_flush(sez):
    for el in sez:
        if slovar[el[0]] < 10:
            return False
    return straight_flush(sez)

def dva_para(sez):
    seznam = []
    koncni = []
    for el in sez:
        seznam.append(slovar[el[0]])
    for el in seznam:
        if seznam.count(el) == 1:
            koncni.append(el)
    if je_par(sez) and len(koncni) == 1:
        return True
    else:
        return False

def full_house(sez):
    seznam = []
    koncni = []
    for el in sez:
        seznam.append(slovar[el[0]])
    for el in seznam:
        if seznam.count(el) == 1:
            koncni.append(el)
    if je_par(sez) and je_tris(sez) and len(koncni) == 0:
        return True
    else:
        return False

def razvrsti(sez):
    if royal_flush(sez):
        return [9]
    elif straight_flush(sez):
        return [8] + povelikosti(sez)
    elif je_poker(sez):
        seznam = []
        for el in sez:
            seznam.append(slovar[el[0]])
        a = 0
        b = 0
        for el in seznam:
            if seznam.count(el) == 4:
                a = el
            else:
                b = el
        return [7, a, b]
    elif full_house(sez):
        seznam = []
        for el in sez:
            seznam.append(slovar[el[0]])
        a = 0
        b = 0
        for el in seznam:
            if seznam.count(el) == 3:
                a = el
            else:
                b = el
        return [6, a, b]
    elif je_barva(sez):
        return [5] + povelikosti(sez)
    elif je_lestvica(sez):
        return [4] + povelikosti(sez)
    elif je_tris(sez):
        seznam = []
        for el in sez:
            seznam.append(slovar[el[0]])
        a = 0
        b = 0
        c = 0
        for el in seznam:
            if seznam.count(el) == 3:
                a = el
            else:
                if el > b:
                    c = b
                    b = el
                else:
                    c = el
        return [3, a, b, c]
    elif dva_para(sez):
        seznam = []
        for el in sez:
            seznam.append(slovar[el[0]])
        a = 0
        b = 0
        c = 0
        for el in seznam:
            if seznam.count(el) == 1:
                c = el
            else:
                if el > a:
                    b = a
                    a = el
                elif el < a:
                    b = el
        return [2, a, b, c]
    elif je_par(sez):
        seznam = []
        for el in sez:
            seznam.append(slovar[el[0]])
        a = 0
        b = 0
        c = 0
        d = 0
        for el in seznam:
            if seznam.count(el) == 2:
                a = el
            else:
                if el > b:
                    d = c
                    c = b
                    b = el
                elif el > c:
                    d = c
                    c = el
                else:
                    d = el
        return [1, a, b, c, d]
    else:
        return [0] + povelikosti(sez)




hands = []
with open(r'C:\Users\jureb\OneDrive\Desktop\Euler\poker.txt', 'r') as data:
    for vrstica in data:
        hands += [vrstica.split()]

counter = 0
for el in hands:
    prva = sorted(el[:5])
    druga = sorted(el[5:])
    if razvrsti(prva) > razvrsti(druga):
        counter += 1
    
print(counter)


