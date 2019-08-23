def gcd(x, y):
    if x % y == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd(y, x % y)

print(-6//gcd(-6, 3), 3//gcd(-6, 3))
print(6//gcd(6, -3), -3//gcd(6, -3))
print(-6//gcd(-6, -3), -3//gcd(-6, -3))