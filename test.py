from math import pi,cos,sqrt

print(pi)
print("chesk")
x=5
print("result is ",x*3)

midpoint = 5

lower=[]
upper=[]

for i in range (10):
    if(i<midpoint):
        lower.append(i)
    else:
        upper.append(i)

print("lower : ", lower)
print("upper : ", upper)

a = ["a","b","c"]
print(a[0]==a[-3])
temp = complex(2,3)
print(temp+3)

L = [n for n in range(2,40)]
print("Liste entière")
print(L)

L = [n for n in range(2,40) if n == L[0] or n % L[0] > 0]
print("Liste sans les chiffres paires")
print(L)

def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2,N):
        if all(n % p for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(40))

print('---'.join(['1','2','3']))

lieux = "plage"
print("toto a la {}".format(lieux))
