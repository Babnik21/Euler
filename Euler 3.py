n = 600851475143


def najvecji_prastevilski_deljitelj(n):
    k = 2
    while k <= n:
        while n % k == 0:
            n = n // k
            maximum = k
        k += 1
    return maximum

print(najvecji_prastevilski_deljitelj(n))


