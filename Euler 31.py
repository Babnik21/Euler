def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n-1)

#najprej poiščemo koliko kovancev potrebujemo da sestavimo 2£ iz enakih kovancev:
#1p => 200, 2p => 100, 5p => 40, 10p => 20, 20p => 10, 50p => 4, 1£ => 2, 2£ => 1
#(slednjega lahko prištejemo samo na koncu ker nima smisla upoštevat unikaten primer)

counter = 0

for funt in range(3):
    vsota = 100*funt
    if vsota == 200:
        counter += 1
        break
    for pol_funta in range(5):
        vsota = 100*funt + 50*pol_funta
        if vsota == 200:
            counter += 1
            break
        for dvajsetka in range(11):
            vsota = 100*funt + 50*pol_funta + 20*dvajsetka
            if vsota == 200:
                counter += 1
                break
            for desetka in range(21):
                vsota = 100* funt + 50* pol_funta + 20* dvajsetka + 10* desetka
                if vsota == 200:
                    counter += 1
                    break
                for petka in range(41):
                    vsota = 100 * funt + 50*pol_funta + 20*dvajsetka + 10*desetka + 5* petka
                    if vsota == 200:
                        counter += 1
                        break
                    for dvica in range(101):
                        vsota = 100*funt + 50*pol_funta + 20*dvajsetka + 10*desetka + 5*petka + 2*dvica
                        if vsota == 200:
                            counter += 1
                            break
                        for enica in range(201):
                            vsota = 100*funt + 50*pol_funta + 20*dvajsetka + 10*desetka + 5*petka + 2*dvica + enica
                            if vsota == 200:
                                counter += 1
                                break
                            elif vsota > 200:
                                break


print(counter + 1)



