def vsota_prvih(n):
    if n == 1:
        return 1
    else:
        return n + vsota_prvih(n-1)

def vsota_prvih_kvadratov(n):
    if n == 1:
        return n
    else:
        return n ** 2 + vsota_prvih_kvadratov(n - 1)

resitev = vsota_prvih(100)**2 - vsota_prvih_kvadratov(100)

print(resitev)
