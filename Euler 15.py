seznam = 20 * ['A'] + 20 * ['B']

def fakulteta(n):
    if n <= 1:
        return 1 
    else:
        return n * fakulteta(n-1)

print(fakulteta(40)//(fakulteta(20) * fakulteta(20)))

