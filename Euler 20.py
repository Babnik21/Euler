
n = 100
produkt = 1

while n > 0:
    produkt = produkt*n
    n -= 1

print(produkt)

vsota = 0

while produkt != 0:
    vsota += produkt%10
    produkt = produkt//10

print(vsota)
