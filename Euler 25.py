

f_1 = 1
f_2 = 1
f_3 = 2
counter = 3

while len(str(f_3)) < 1000:
    f_1 = f_2
    f_2 = f_3
    f_3 = f_1 + f_2
    counter += 1

print(counter)