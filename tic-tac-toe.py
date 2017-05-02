"""Init game"""
row = 3
game = [0] * 3 ** 2

def display(game,row = 3):
    iters = [iter(game)] * row
    for line in zip(*iters):
        print("|".join(f"{item:^3}" for item in line))

def changeCase(game,posX,posY,tourPlayer1):
    char = "2"
    if(tourPlayer1):
        char = "1"
    game[posX + 3 * posY] = char
    return not(tourPlayer1)

strTourPlayer = "Tour J1"
tourPlayer1 = True

display(game)
print(strTourPlayer)
play = input()

while play != "Q":
    posPlay = play.split()
    tourPlayer1 = changeCase(game,int(posPlay[0]),int(posPlay[1]),tourPlayer1)
    display(game)
    if tourPlayer1 :
        strTourPlayer = "Tour J1"
    else :
        strTourPlayer = "Tour J2"
    print(strTourPlayer)
    play = input()
