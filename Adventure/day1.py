from pathlib import Path

pathCarte = Path("map.txt")

with pathCarte.open("r") as f:
    carte = [str(i).strip() for i in f]

#print(carte)
carte = [ carte.strip() for carte in carte[0].split(",")]
#print(carte)

def resetMemory(memory, letter):
    if memory.count(letter) >=4:
        memory = [ i for i in memory if i != letter]
    return memory

count = 0

memory = []
for i in range(len(carte)):
    tempNow = list(carte[i])
    #print(tempNow)
    memory.append(tempNow[0])
    print(memory)
    if(memory.count("R") >= 3 or memory.count("L") >= 3):
        count -= int("".join(tempNow[1:]))
        print("c'est la merde {0}".format(int("".join(tempNow[1:]))))
    else:
        count += int("".join(tempNow[1:]))


    memory = resetMemory(memory, "R")
    memory = resetMemory(memory, "L")



print(count)
