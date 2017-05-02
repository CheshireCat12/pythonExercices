func = lambda x:x*53
for val in map(func,range(10)):
    print(val)

A0 = dict(zip(("a","b","c","d","e"),(1,2,"er",4,5)))
print(A0)
A1 = [i for i in range(10)]
print(A1)
for indice, value in enumerate(A1):
    print("{0} possède la valeur : {1}".format(indice,value))

for value in A0:
    print("{0} possède la valeur : {1}".format(value,A0[value]))

A2 = range(10)
print(A2)


for s in A0:
    print(s)

A5 = {i:i*i for i in A1}
print(A5)

A6 = zip((1, 2, 3, 4), ('a', 'b', 'c', 'd'))

A7, A8= zip(*A6)
print(A7, A8)

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)




for i in range(len(carte)):
    tempNow = list(carte[i])
    print(tempNow)
    if i-1<0:
        tempLast = [0,0]
    else:
        tempLast = list(carte[i-1])
    if tempNow[0] != tempLast[0] or change:
        count += int("".join(tempNow[1:]))
        change = False
    else:
        count -= int("".join(tempNow[1:]))
        change = True
        print("change")
