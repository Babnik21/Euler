def prime_factors(n):
    i = 2
    a = set()
    while i < n**0.5 or n == 1:
        if n % i == 0:
            n = n//i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

i = 2*3*5*7     #najmanjse stevilo s 4 razlicnimi deljitelji

while True:
    if prime_factors(i) == 4:
        i += 1
        if prime_factors(i) == 4:
            i += 1
            if prime_factors(i) == 4:
                i += 1
                if prime_factors(i) == 4:
                    print(i-3)
                    break
    i += 1






