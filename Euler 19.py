dnevi = {
    '0':'nedelja',
    '1':'ponedeljek',
    '2':'torek',
    '3':'sreda',
    '4':'cetrtek',
    '5':'petek',
    '6':'sobota'
}

#lahko ignoriramo pravila za prestopno leto za deljivost s 100 in 400 saj se ne srečamo z njima, za nas bo vsako 4. leto prestopno
def prestopno(leto):
    if leto%4 == 0:
        return True
    else:
        return False

prvi = 366%7

dan = prvi
dan_counter = 1
mesec = 1
leto = 1901
stevec = 0

while leto < 2001:
    if mesec == 12 and dan_counter == 31:
        leto += 1
        mesec = 1
        dan_counter = 0
    elif mesec in [1, 3, 5, 7, 8, 10] and dan_counter == 31:
        mesec += 1
        dan_counter = 0
    elif prestopno(leto) and mesec == 2 and dan_counter == 29:
        mesec += 1
        dan_counter = 0
    elif not prestopno(leto) and mesec == 2 and dan_counter == 28:
        mesec += 1
        dan_counter = 0
    elif mesec in [4, 6, 9, 11] and dan_counter == 30:
        mesec += 1
        dan_counter = 0
    dan += 1
    dan_counter += 1
    dan = dan%7
    if dan == 0 and dan_counter == 1:
        stevec += 1

print(stevec)
    

    
    
    
    