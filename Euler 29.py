
aji = list(range(2, 101))
bji = list(range(2, 101))

seznam = []
for a in aji:
    for b in bji:
        if a**b not in seznam:
            seznam += [a**b]

print(len(seznam))





