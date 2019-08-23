def st_deljiteljev(n):
    rezultat = 0
    if n ** 0.5 == n**0.5//1:
        rezultat = 1
    i = 1
    while i < n**0.5:
        if n % i == 0:
            rezultat += 2
        i += 1
    return rezultat

print(st_deljiteljev(2800054))

i = 2
n = 1
while st_deljiteljev(n) < 500:
    n += i
    i += 1
    

print(n)



