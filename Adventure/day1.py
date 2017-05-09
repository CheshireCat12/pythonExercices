from pathlib import Path
from turtle import shape, forward, left, right, speed, exitonclick,position

shape("turtle")
left(90)
pathCarte = Path("map.txt")
print(position())
with pathCarte.open("r") as f:
    carte = [str(i).strip() for i in f]

carte = [ carte.strip() for carte in carte[0].split(",")]

def drawTurtle(direction,length):
    if direction == "R":
        right(90)
    elif direction == "L":
        left(90)
    forward(length)

speed(0)

memories = []
twice = []
test = True
axePos = {"X":0,"Y":0}
axe = "X"
lastAxe = "+"
for i in range(len(carte)):
    tempNow = list(carte[i])
    if axe == "X":
        if lastAxe == "+":
            if tempNow[0] == "R":
                axePos[axe] += int("".join(tempNow[1:]))
                lastAxe = "+"
            else:
                axePos[axe] -= int("".join(tempNow[1:]))
                lastAxe = "-"
        else:
            if tempNow[0] == "R":
                axePos[axe] -= int("".join(tempNow[1:]))
                lastAxe = "-"
            else:
                axePos[axe] += int("".join(tempNow[1:]))
                lastAxe = "+"
        axe = "Y"
    else:
        if lastAxe == "+":
            if tempNow[0] == "R":
                axePos[axe] -= int("".join(tempNow[1:]))
                lastAxe = "-"
            else:
                axePos[axe] += int("".join(tempNow[1:]))
                lastAxe = "+"
        else:
            if tempNow[0] == "R":
                axePos[axe] += int("".join(tempNow[1:]))
                lastAxe = "+"
            else:
                axePos[axe] -= int("".join(tempNow[1:]))
                lastAxe = "-"
        axe = "X"

    drawTurtle(tempNow[0],int("".join(tempNow[1:])))
    newPos = position()
    if newPos in memories and test:
        twice = newPos
        test = False
    memories.append(newPos)


posx, posy = position()

print(axePos)
print(twice)

print(posx+posy)
exitonclick()
