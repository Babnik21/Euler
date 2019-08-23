enice = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
teens = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8  # tu štejemo tudi ten
desetice = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6
hundred = 7
hundred_and = 10
tisoc = 11
#do vključno z 99:

vsota = desetice * 10 + teens + enice * 9
print(vsota)

#do vključno z 1000:
vsota = vsota*10 + (enice + 9*hundred_and)*99 + enice + hundred*9 + 11

print(vsota)




    


