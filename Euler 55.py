
def palindrom(niz):
    if len(niz) <= 1:
        return True
    if niz[0] == niz[-1]:
        return palindrom(niz[1:-1])
    else:
        return False
    
def reverse(niz):
    return niz[::-1]

stevilo = 1
counter = 0

while stevilo <= 10000:
    poskusov = 0
    tester = stevilo
    while poskusov < 50:
        if palindrom(str(tester + int(reverse(str(tester))))):      #vsako število, ki naredi palindrom, poveča counter za 1 (štejemo napačne)
            counter += 1                                            #na koncu to popravimo tako, da odštejemo coutner od vseh števil
            break
        else:
            tester += int(reverse(str(tester)))
            poskusov += 1
    stevilo += 1

print(stevilo - 1 - counter)  #stevilo je na tej tocki 10001, namesto 10000, zato še - 1

