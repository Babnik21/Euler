def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n-1)

def kombinacije(n, r):
    return fakulteta(n)//(fakulteta(r) * fakulteta(n-r))

n = 20
counter = 0
while n <= 100:
    for r in range(1, n):
        if kombinacije(n, r) >= 1000000:
            counter += 1
    n += 1

print(counter)