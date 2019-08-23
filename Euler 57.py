def gcd(x, y):
    if x == 0 or y == 0:
        return 0
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

class Ulomek:                   #izkaže se da ne potrebujemo tega
    def __init__(self, st, im):
        self.im = im//gcd(st, im)
        self.st = st//gcd(st, im)

    def __add__(self, other):
        return Ulomek(self.st * other.im + self.im*other.st, other.im * self.im)

    def __str__(self):
        return '{0}/{1}'.format(self.st, self.im)

    def __mul__(self, other):
        return Ulomek(self.st * other.st, self.im * other.im)

    def __truediv__(self, other):
        return Ulomek(self.st * other.im, self.im * other.st)

#ugotovimo, da je n + prvi približek oblike a_(n+1)/b_(n+1), če je a_(n+1) = a_n + 2*b_n in b_(n+1) = a_n + b_n
#s to ugotovitvijo je stvar enostavna

imenovalec = 2
števec = 3
n = 1
counter = 0

while n <= 1000:
    if len(str(števec)) > len(str(imenovalec)):
        counter += 1
    a = števec
    števec = števec + 2* imenovalec
    imenovalec += a
    n += 1

print(counter) 

