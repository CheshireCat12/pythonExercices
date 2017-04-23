from itertools import count
from random import random
from collections import Counter
#la probabilité de tombé sur un carte (Légendaire, Epique, Rare, Commune)
testCartes = {0.01:"L",0.05:"E",0.28:"R",1.0:"C"}

finalResult = []
nbTirages = 10000

for i in count():
    resultat = []
    for i in range(5):
        rand = random()
        selectCarte = [carte for val,carte in testCartes.items() if val > rand]
        resultat.append(selectCarte[0])
    if all("C" in s for s in resultat):
        print("Tirage non valide.")
    else:
        print(resultat)
        for x in resultat:
            finalResult.append(x)
    if len(finalResult) >=nbTirages*5:
        break;

for letter, count in Counter(finalResult).most_common(4):
    print("Valeur : {0}, apparait : {1}, pourcentage {2:.2f}%".format(letter,count,(count/len(finalResult))*100))
