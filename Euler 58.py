import pyprimesieve

i = 1
step = 2
robni = 1
robna_prastevila = 0
prastevila = []

minimum = 0.1

def prastevilo(n):
    for i in range(3, int(((n ** 0.5) // 1) + 1), 2):
        if n % i == 0:
            return False
    return True

print(prastevilo(121))
print(prastevilo(37))

while minimum >= 0.1:
    for _ in range(4):
        i += step
        robni += 1
        if prastevilo(i):
            robna_prastevila += 1
    step += 2
    minimum = min(minimum, robna_prastevila/robni)

print(step + 1)
    
