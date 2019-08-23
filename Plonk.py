def memoiziraj(f):
    rezultati = {}
    def mem_f(x):
        if x not in rezultati:
            rezultati[x] = f(x)
        return rezultati[x]
    return mem_f

#naredi pametno funkcijo

import sys
sys.setrecursionlimit(10000000)

def vsota(n):
    if n == 0:
        return 0
    else:
        return n + vsota(n-1)

print(vsota(1000))