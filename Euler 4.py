def je_palindrom(n):
    n = str(n)
    if len(n) <= 1:
        return True
    else:
        if n[0] != n[-1]:
            return False
        else:
            return je_palindrom(n[1:-1])

resitev = 0
for i in range(100, 999):
    for j in range(100, 999):
        n = i * j
        if je_palindrom(n) and n > resitev:
            resitev = n

print(resitev)

    