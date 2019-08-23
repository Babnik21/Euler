i = 2
stevilo = 1
vsota = 1
counter = 0
while stevilo < 1001*1001:
    while counter < 4:
        counter += 1
        stevilo += i
        vsota += stevilo
    i += 2
    counter = 0

print(vsota)