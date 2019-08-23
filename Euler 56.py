#presenetljivo lahek problem?
aji = list(range(100))
bji = list(range(100))
najvec = 0

def vsota_stevk(n):
    vsota = 0
    for el in str(n):
        vsota += int(el)
    return vsota

for a in aji:
    for b in bji:
        if vsota_stevk(a ** b) > najvec:
            najvec = vsota_stevk(a ** b)

print(najvec)
        

