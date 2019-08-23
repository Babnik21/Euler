
i = 1
j = 1
k = 2
vsota = 0
while k < 4000000:
    if k% 2 == 0:
        vsota += k
    i = j
    j = k
    k = i + j

print(vsota)