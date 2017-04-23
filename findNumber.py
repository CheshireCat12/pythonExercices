from random import random,seed,randint,choice

maximum = 50
list = [i for i in range(maximum)]
numberChoice = choice(list)

print("Saisissez un nombre (entre 0 & {}) :".format(maximum),end=" ")
n = int(input())

while n != numberChoice :
    resultat = ""
    if n > numberChoice:
        print("Trop grand")
    else:
        print("Trop petit")
    print("Proposition : ",end="")
    n = int(input())

print("Bien jouez vous avez trouver le bon nombre ^^")

print("Voulez-vous tirer un paquet hearstone ?",end=' ')
n = input()

testCartes = {0.01:"L",0.05:"E",0.28:"R",1.0:"C"}

while n != 'non' or n != 'n':
    resultat = []
    for i in range(5):
        rand = random()
        selectCarte = [carte for val,carte in testCartes.items() if val > rand]
        resultat.append(selectCarte[0])
    if all("C" in s for s in resultat):
        print("Tirage non valide.")
    else:
        print(resultat)
    print("Voulez-vous tirer un paquet hearstone ?",end=' ')
    n = input()
